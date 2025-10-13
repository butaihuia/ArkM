import sys
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox,
                               QListWidgetItem)
from PySide6.QtCore import  QTimer, QUrl, QTime, QThread, Signal
from PySide6.QtGui import QKeySequence, QShortcut,  QIcon
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from ArkM import Ui_MainWindow
from Start import Start_MainWindow

import arknight_beta

from ark_style import ARK_STYLESHEET, START_STYLESHEET
from enhanced_logger import EnhancedLogger


class DownloadThread(QThread):
    """下载线程"""
    finished = Signal(bool, str)  # success, message
    progress = Signal(str, int, int)  # filename, downloaded, total

    def __init__(self, music_name):
        super().__init__()
        self.music_name = music_name

    def run(self):
        try:
            if self.music_name not in arknight_beta.name2cid:
                self.finished.emit(False, f"歌曲不存在: {self.music_name}")
                return

            cid = arknight_beta.name2cid[self.music_name]

            # 定义进度回调函数
            def progress_callback(filename, downloaded, total):
                self.progress.emit(filename, downloaded, total)

            success = arknight_beta.download_music(cid, progress_callback)

            if success:
                self.finished.emit(True, f"下载成功: {self.music_name}")
            else:
                self.finished.emit(False, f"下载失败: {self.music_name}")

        except Exception as e:
            self.finished.emit(False, f"下载过程中出错: {str(e)}")


class DeleteThread(QThread):
    """删除线程"""
    finished = Signal(bool, str)  # success, message

    def __init__(self, music_name):
        super().__init__()
        self.music_name = music_name

    def run(self):
        try:
            success, message = arknight_beta.delete_music(self.music_name)
            self.finished.emit(success, message)
        except Exception as e:
            self.finished.emit(False, f"删除过程中出错: {str(e)}")


class ArkMusic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 设置窗口图标
        self.setWindowIcon(QIcon("prts.ico"))

        # 应用样式表
        self.apply_scifi_style()

        # 初始化数据
        self.download_items = []
        self.music_items = []
        self.current_playing_music = None
        self.download_thread = None
        self.delete_thread = None
        self.last_music = "114514"

        # 设置定时器
        self.download_timer = QTimer()
        self.music_timer = QTimer()
        self.progress_timer = QTimer()
        self.download_timer.setSingleShot(True)
        self.music_timer.setSingleShot(True)

        # 初始化媒体播放器
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.audio_output.setVolume(0.5)

        # 初始化增强日志系统
        self.logger = EnhancedLogger(self.logBrowser,self.downloadBrowser)

        # 设置信号连接
        self.setup_connection()

        # 设置快捷键
        self.setup_shortcuts()

        # 设置窗口属性
        self.setWindowTitle("PRTS音乐系统 - 音乐终端")
        self.setMinimumSize(1000, 700)

        # 设置窗口居中显示
        self.center_window()

        # 初始化数据
        self.init_data()

        # 连接定时器超时信号
        self.download_timer.timeout.connect(self.download_items_search)
        self.music_timer.timeout.connect(self.music_items_search)
        self.progress_timer.timeout.connect(self.update_progress)

        # 初始化播放控制
        self.init_media_controls()

        self.logger.log("PRTS音乐系统初始化完成", "SUCCESS")
        self.logger.log("欢迎使用终端音乐管理系统", "INFO")

    def center_window(self):
        """将窗口居中显示"""
        screen = QApplication.primaryScreen().availableGeometry()
        size = self.geometry()
        self.move(
            (screen.width() - size.width()) // 2,
            (screen.height() - size.height()) // 2
        )

    def apply_scifi_style(self):
        """应用样式表"""
        self.setStyleSheet(ARK_STYLESHEET)

    def setup_connection(self):
        """设置信号连接"""
        self.logger.log("正在连接信号...")

        # 搜索功能
        self.downloadSearchInput.textChanged.connect(self.start_download_timer)
        self.downloadSearchButton.clicked.connect(self.download_items_search)
        self.musicSearchInput.textChanged.connect(self.start_music_timer)
        self.musicSearchButton.clicked.connect(self.music_items_search)

        # 刷新功能
        self.downloadRefreshButton.clicked.connect(self.refresh_download_items)
        self.musicRefreshButton.clicked.connect(self.refresh_music_items)

        # 列表项双击事件
        self.downloadlistWidget.itemDoubleClicked.connect(self.on_download_item_double_clicked)
        self.musicListWidget.itemDoubleClicked.connect(self.on_music_item_double_clicked)

        # 操作按钮
        self.downloadButton.clicked.connect(self.download_button_clicked)
        self.deletButton.clicked.connect(self.delete_button_clicked)
        self.clearLogButton.clicked.connect(self.clear_log)

        self.logger.log("信号连接设置完成", "SUCCESS")

    def setup_shortcuts(self):
        """设置快捷键"""
        # 下载列表快捷键"Ctrl+F"
        download_search_shortcut = QShortcut(QKeySequence("Ctrl+F"), self)
        download_search_shortcut.activated.connect(self.downloadSearchInput.setFocus)

        # 音乐列表快捷键"Ctrl+G"
        music_search_shortcut = QShortcut(QKeySequence("Ctrl+G"), self)
        music_search_shortcut.activated.connect(self.musicSearchInput.setFocus)

        # 下载快捷键"Ctrl+D"
        download_shortcut = QShortcut(QKeySequence("Ctrl+D"), self)
        download_shortcut.activated.connect(self.download_button_clicked)

        # 删除快捷键"Ctrl+Delete"
        delete_shortcut = QShortcut(QKeySequence("Ctrl+Delete"), self)
        delete_shortcut.activated.connect(self.delete_button_clicked)

        # 清空日志快捷键"Ctrl+L"
        clear_log_shortcut = QShortcut(QKeySequence("Ctrl+L"), self)
        clear_log_shortcut.activated.connect(self.clear_log)

        self.logger.log("快捷键设置完成", "SUCCESS")

    def init_media_controls(self):
        """初始化媒体控制"""
        # 连接媒体播放器信号
        self.player.positionChanged.connect(self.position_changed)
        self.player.durationChanged.connect(self.duration_changed)
        self.player.playbackStateChanged.connect(self.playback_state_changed)

        # 连接控制按钮
        self.playButton.clicked.connect(self.play_music_from_button)
        self.pauseButton.clicked.connect(self.pause_music)
        self.stopButton.clicked.connect(self.stop_music)

        # 连接滑块
        self.progressSlider.sliderMoved.connect(self.set_position)
        self.volumeSlider.valueChanged.connect(self.set_volume)

        # 设置音量滑块初始值
        self.volumeSlider.setValue(50)

        self.logger.log("媒体控制初始化完成", "SUCCESS")

    def init_data(self):
        """初始化数据"""
        try:
            # 初始化下载列表
            undownloaded_music = arknight_beta.get_undownloaded_music()
            self.download_items = undownloaded_music

            # 初始化音乐列表
            downloaded_music = arknight_beta.get_downloaded_music()
            self.music_items = downloaded_music

            # 刷新显示
            self.refresh_download_items()
            self.refresh_music_items()

            self.logger.log(f"系统就绪: 待下载 {len(self.download_items)} 首, 已下载 {len(self.music_items)} 首",
                            "SUCCESS")
        except Exception as e:
            self.logger.log(f"数据初始化失败: {str(e)}", "ERROR")

    def start_download_timer(self):
        """启动下载搜索定时器"""
        self.download_timer.start(500)

    def start_music_timer(self):
        """启动音乐搜索定时器"""
        self.music_timer.start(500)

    def download_items_search(self):
        """执行下载列表搜索"""
        search_text = self.downloadSearchInput.text().strip()
        self.logger.log(f"搜索待下载曲目: '{search_text}'", "INFO")
        self.refresh_download_items()

    def music_items_search(self):
        """执行音乐列表搜索"""
        search_text = self.musicSearchInput.text().strip()
        self.logger.log(f"搜索本地曲库: '{search_text}'", "INFO")
        self.refresh_music_items()

    def refresh_download_items(self):
        """刷新下载列表显示"""
        try:
            search_text = self.downloadSearchInput.text().strip().lower()
            self.downloadlistWidget.clear()

            filtered_items = [item for item in self.download_items
                              if not search_text or search_text in item.lower()]

            for item_text in filtered_items:
                item = QListWidgetItem(item_text)
                self.downloadlistWidget.addItem(item)

            count = self.downloadlistWidget.count()
            self.logger.log(f"刷新待下载列表: 显示 {count} 首歌曲", "INFO")
        except Exception as e:
            self.logger.log(f"刷新下载列表失败: {str(e)}", "ERROR")

    def refresh_music_items(self):
        """刷新音乐列表显示"""
        try:
            search_text = self.musicSearchInput.text().strip().lower()
            self.musicListWidget.clear()

            filtered_items = [item for item in self.music_items
                              if not search_text or search_text in item.lower()]

            for item_text in filtered_items:
                item = QListWidgetItem(item_text)
                self.musicListWidget.addItem(item)

            count = self.musicListWidget.count()
            self.logger.log(f"刷新已下载列表: 显示 {count} 首歌曲", "INFO")
        except Exception as e:
            self.logger.log(f"刷新音乐列表失败: {str(e)}", "ERROR")

    def on_download_item_double_clicked(self, item):
        """下载列表双击事件 - 下载歌曲"""
        music_name = item.text()
        self.logger.log(f"准备下载: {music_name}", "INFO")

        reply = QMessageBox.question(self, "确认下载",
                                     f"确定要下载《{music_name}》吗？",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.Yes)

        if reply == QMessageBox.StandardButton.Yes:
            self.download_music(music_name)

    def on_music_item_double_clicked(self, item):
        """音乐列表双击事件 - 播放歌曲"""
        music_name = item.text()
        self.play_music(music_name)

    def download_button_clicked(self):
        """下载按钮点击事件"""
        current_row = self.downloadlistWidget.currentRow()
        if current_row >= 0:
            item = self.downloadlistWidget.item(current_row)
            music_name = item.text()
            self.download_music(music_name)
        else:
            self.logger.log("请先在待下载列表中选择一首歌曲", "WARNING")
            QMessageBox.warning(self, "提示", "请先在待下载列表中选择一首歌曲")

    def delete_button_clicked(self):
        """删除按钮点击事件"""
        current_row = self.musicListWidget.currentRow()
        if current_row >= 0:
            item = self.musicListWidget.item(current_row)
            music_name = item.text()
            self.delete_music(music_name)
        else:
            self.logger.log("请先在已下载列表中选择一首歌曲", "WARNING")
            QMessageBox.warning(self, "提示", "请先在已下载列表中选择一首歌曲")

    def download_music(self, music_name):
        """下载音乐"""
        if self.download_thread and self.download_thread.isRunning():
            self.logger.log("当前有下载任务正在进行，请稍候", "WARNING")
            return

        self.download_thread = DownloadThread(music_name)
        self.download_thread.finished.connect(self.on_download_finished)
        self.download_thread.progress.connect(self.on_download_progress)
        self.download_thread.start()

        # 禁用下载按钮
        self.downloadButton.setEnabled(False)
        self.logger.log(f"开始下载: {music_name}", "INFO")

    def on_download_progress(self, filename, downloaded, total):
        """下载进度更新"""
        self.logger.update_progress(filename, downloaded, total)

    def on_download_finished(self, success, message):
        """下载完成回调"""
        # 重新启用下载按钮
        self.downloadButton.setEnabled(True)
        # 清除进度消息标记
        self.logger.clear_progress()

        if success:
            self.logger.log(message, "SUCCESS")
            # 刷新数据
            self.init_data()
            QMessageBox.information(self, "成功", f"下载成功！")
        else:
            self.logger.log(message, "ERROR")
            QMessageBox.warning(self, "失败", message)

    def delete_music(self, music_name):
        """删除音乐"""
        reply = QMessageBox.question(self, "确认删除",
                                     f"确定要删除《{music_name}》吗？此操作不可撤销！",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            if self.delete_thread and self.delete_thread.isRunning():
                self.logger.log("当前有删除任务正在进行，请稍候", "WARNING")
                return

            self.delete_thread = DeleteThread(music_name)
            self.delete_thread.finished.connect(self.on_delete_finished)
            self.delete_thread.start()

    def on_delete_finished(self, success, message):
        """删除完成回调"""
        if success:
            self.logger.log(message, "SUCCESS")
            # 刷新数据
            self.init_data()
            QMessageBox.information(self, "成功", f"删除成功！")
        else:
            self.logger.log(message, "ERROR")
            QMessageBox.warning(self, "失败", message)

    def play_music(self, music_name):
        """播放音乐"""
        try:
            if music_name == self.last_music and self.player.playbackState() == QMediaPlayer.PlaybackState.PausedState:
                self.player.play()
            else:
                # 如果正在播放其他音乐，先停止
                if self.current_playing_music and self.current_playing_music != music_name:
                    self.stop_music()

                # 查找音乐文件
                music_dir = "../songs/"
                if not os.path.exists(music_dir):
                    self.logger.log("音乐目录不存在", "ERROR")
                    QMessageBox.warning(self, "错误", "音乐目录不存在")
                    return

                # 查找匹配的文件
                found_files = []
                for file in os.listdir(music_dir):
                    if music_name in file and file.endswith(('.mp3', '.wav', '.ogg', '.flac')):
                        found_files.append(file)

                if not found_files:
                    self.logger.log(f"未找到歌曲文件: {music_name}", "WARNING")
                    QMessageBox.warning(self, "提示", f"未找到《{music_name}》的音频文件")
                    return

                # 如果有多个匹配文件，选择第一个
                file_path = os.path.join(music_dir, found_files[0])

                # 设置媒体源并播放
                self.player.setSource(QUrl.fromLocalFile(file_path))
                self.current_playing_music = music_name

                # 开始播放
                self.player.play()

                # 启动进度更新定时器
                self.progress_timer.start(100)

                self.logger.log(f"正在播放: {music_name}", "SUCCESS")
                self.last_music = music_name

        except Exception as e:
            self.logger.log(f"播放失败: {str(e)}", "ERROR")
            QMessageBox.critical(self, "错误", f"播放失败: {str(e)}")

    def play_music_from_button(self):
        """从播放按钮触发的播放"""
        current_row = self.musicListWidget.currentRow()
        if current_row >= 0:
            item = self.musicListWidget.item(current_row)
            music_name = item.text()
            self.play_music(music_name)
        else:
            # 如果没有选择歌曲，尝试继续播放当前歌曲
            if self.player.playbackState() == QMediaPlayer.PlaybackState.PausedState:
                self.player.play()
                self.logger.log("继续播放", "INFO")
            else:
                self.logger.log("请先在已下载列表中选择一首歌曲", "WARNING")
                QMessageBox.warning(self, "提示", "请先在已下载列表中选择一首歌曲")

    def pause_music(self):
        """暂停音乐"""
        if self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.player.pause()
            self.logger.log("暂停播放", "INFO")

    def stop_music(self):
        """停止音乐 - 完全释放文件资源"""
        if self.player.playbackState() != QMediaPlayer.PlaybackState.StoppedState:
            # 先暂停播放
            self.player.pause()

            # 设置源为空，释放文件句柄
            self.player.setSource(QUrl())
            # 等待一小段时间确保资源释放
            QApplication.processEvents()

            # 完全停止播放器
            self.player.stop()

            # 重置状态
            self.current_playing_music = None
            self.progressSlider.setValue(0)
            self.update_progress()
            self.progress_timer.stop()
            self.label_3.setText(f"播放进度: 00:00/00:00")
            self.logger.log("停止播放并释放资源", "INFO")

    def set_position(self, position):
        """设置播放位置"""
        self.player.setPosition(position)

    def set_volume(self, volume):
        """设置音量"""
        self.audio_output.setVolume(volume / 100.0)
        self.logger.log(f"音量设置为: {volume}%", "INFO")

    def position_changed(self, position):
        """播放位置改变时更新滑块"""
        if not self.progressSlider.isSliderDown():
            self.progressSlider.setValue(position)

    def duration_changed(self, duration):
        """播放时长改变时更新滑块范围"""
        self.progressSlider.setRange(0, duration)

    def playback_state_changed(self, state):
        """播放状态改变"""
        if state == QMediaPlayer.PlaybackState.PlayingState:
            self.playButton.setText("播放中")
        elif state == QMediaPlayer.PlaybackState.PausedState:
            self.playButton.setText("播放")
        elif state == QMediaPlayer.PlaybackState.StoppedState:
            self.playButton.setText("播放")
            self.progressSlider.setValue(0)

    def update_progress(self):
        """更新进度显示"""
        if self.player.duration() > 0:
            current_time = QTime(0, 0).addMSecs(self.player.position())
            total_time = QTime(0, 0).addMSecs(self.player.duration())
            time_str = f"{current_time.toString('mm:ss')}/{total_time.toString('mm:ss')}"
            self.label_3.setText(f"播放进度: {time_str}")

    def clear_log(self):
        """清空日志"""
        self.logger.clear()
        self.logger.log("日志已清空", "INFO")


class StartMusic(QMainWindow, Start_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 设置窗口图标
        self.setWindowIcon(QIcon("prts.ico"))

        # 应用样式表
        self.apply_scifi_style()

    def apply_scifi_style(self):
        self.setStyleSheet(START_STYLESHEET)


def main():
    """主函数"""
    try:
        # 初始化下载引擎
        arknight_beta.download_engine_init()

        # 创建应用
        app = QApplication(sys.argv)

        # 设置应用样式
        app.setStyle('Fusion')

        # 设置应用属性
        app.setApplicationName("PRTS音乐系统")
        app.setApplicationVersion("2.0.0")

        # 创建主窗口
        window = ArkMusic()
        window.show()

        # 运行应用
        sys.exit(app.exec())

    except Exception as e:
        print(f"系统启动失败: {e}")
        QMessageBox.critical(None, "启动错误", f"PRTS系统启动失败: {e}")




# def main():
#     StartApp = QApplication(sys.argv)
#     StartApp.setStyle('Fusion')
#     StartWindow = StartMusic()
#     StartWindow.show()
#     sys.exit(StartApp.exec())



if __name__ == '__main__':
    main()