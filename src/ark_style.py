# ark_style.py
"""
简约黑灰白色调样式表 - 明日方舟PRTS系统主题
"""

START_STYLESHEET="""
/* styles.qss */
QMainWindow {
    background-color: #2b2b2b;

}
/*
QLabel#titleLable {
    background-color: rgba(43, 43, 43, 150);
    color: white;
    font-weight: bold;
    font-size: 14px;
    padding: 10px;
    border-radius: 5px;
    border: none;
    
    background-image: url(111.jpg);
    background-repeat: no-repeat;
    background-position: center;
    background-size:contain ;
}
*/

QLabel#titleLable {
    color: white;
    font-weight: bold;
    font-size: 14px;
    background-color: #2b2b2b;
    padding: 10px;
    border-radius: 5px;
    

}

QLabel#label {
    color: white;
    font-weight: bold;
    background-color: #2b2b2b;
    padding: 5px;
    border-radius: 3px;
}

QPushButton#okButton {
    color: white;
    font-weight: bold;
    background-color: #3d3d3d;
    border: 1px solid #555555;
    padding: 8px 15px;
    border-radius: 5px;
}

QPushButton#okButton:hover {
    background-color: #4d4d4d;
}

QPushButton#okButton:pressed {
    background-color: #2d2d2d;
}

QLineEdit#InputEdit {
    background-color: #3d3d3d;
    color: white;
    border: 1px solid #555555;
    padding: 5px;
    border-radius: 3px;
}

QLineEdit#InputEdit:focus {
    border: 1px solid #0078d4;
}

QStatusBar {
    background-color: #2b2b2b;
    color: #888888;
}

QMenuBar {
    background-color: #2b2b2b;
    color: white;
}

QMenuBar::item:selected {
    background-color: #3d3d3d;
}
"""


ARK_STYLESHEET = """
/* ===== 主窗口样式 ===== */
QMainWindow {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                               stop:0 #1a1a1a, stop:0.5 #2a2a2a, stop:1 #1a1a1a);
    color: #e0e0e0;
}

QWidget#centralwidget {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                               stop:0 #1a1a1a, stop:0.5 #2a2a2a, stop:1 #1a1a1a);
}

/* ===== 标签样式 ===== */
QLabel {
    background: transparent;
    color: #e0e0e0;
    font-family: "Microsoft YaHei UI", "Segoe UI";
    font-size: 12px;
    font-weight: bold;
    padding: 6px 10px;
    border: 1px solid #555555;
    border-radius: 4px;
    background-color: rgba(40, 40, 40, 0.8);
}

/* ===== 按钮基础样式 ===== */
QPushButton {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                               stop:0 #404040, stop:0.5 #303030, stop:1 #404040);
    border: 1px solid #666666;
    border-radius: 6px;
    color: #e0e0e0;
    font-family: "Microsoft YaHei UI", "Segoe UI";
    font-size: 11px;
    font-weight: bold;
    padding: 8px 16px;
    min-width: 70px;
}

QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                               stop:0 #505050, stop:0.5 #404040, stop:1 #505050);
    border: 1px solid #888888;
    color: #ffffff;
}

QPushButton:pressed {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                               stop:0 #303030, stop:0.5 #202020, stop:1 #303030);
    border: 1px solid #444444;
}

QPushButton:disabled {
    background: #2a2a2a;
    border: 1px solid #444444;
    color: #666666;
}

/* ===== 特殊按钮样式 ===== */
QPushButton#downloadButton {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                               stop:0 #606060, stop:0.5 #505050, stop:1 #606060);
    border: 1px solid #888888;
    color: #ffffff;
}

QPushButton#downloadButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                               stop:0 #707070, stop:0.5 #606060, stop:1 #707070);
    border: 1px solid #aaaaaa;
}

QPushButton#deletButton {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                               stop:0 #703030, stop:0.5 #602020, stop:1 #703030);
    border: 1px solid #884444;
    color: #ffffff;
}

QPushButton#deletButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                               stop:0 #804040, stop:0.5 #703030, stop:1 #804040);
    border: 1px solid #aa6666;
}

/* ===== 播放控制按钮样式 ===== */
QPushButton#playButton,
QPushButton#pauseButton,
QPushButton#stopButton {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                               stop:0 #406060, stop:0.5 #305050, stop:1 #406060);
    border: 1px solid #608888;
    color: #ffffff;
    min-width: 80px;
}

QPushButton#playButton:hover,
QPushButton#pauseButton:hover,
QPushButton#stopButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                               stop:0 #507070, stop:0.5 #406060, stop:1 #507070);
    border: 1px solid #80aaaa;
}

/* ===== 输入框样式 ===== */
QLineEdit {
    background: rgba(30, 30, 30, 0.9);
    border: 1px solid #555555;
    border-radius: 6px;
    color: #e0e0e0;
    font-family: "Consolas", "Microsoft YaHei UI";
    font-size: 11px;
    padding: 8px 12px;
    selection-background-color: #606060;
}

QLineEdit:focus {
    border: 1px solid #888888;
    background: rgba(35, 35, 35, 0.9);
}

/* ===== 列表控件样式 ===== */
QListWidget {
    background: rgba(25, 25, 25, 0.9);
    border: 1px solid #555555;
    border-radius: 6px;
    color: #e0e0e0;
    font-family: "Microsoft YaHei UI", "Segoe UI";
    font-size: 11px;
    outline: none;
}

QListWidget::item {
    background: transparent;
    border: none;
    padding: 8px 12px;
    margin: 2px;
    border-radius: 4px;
    border-bottom: 1px solid rgba(70, 70, 70, 0.5);
}

QListWidget::item:selected {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                               stop:0 #606060, stop:1 #505050);
    color: #ffffff;
    border: none;
}

QListWidget::item:hover {
    background: rgba(60, 60, 60, 0.6);
    border: none;
}

/* ===== 文本浏览器样式（日志） ===== */
QTextBrowser {
    background: rgba(20, 20, 20, 0.95);
    border: 1px solid #555555;
    border-radius: 6px;
    color: #e0e0e0;
    font-family: "Consolas", "Microsoft YaHei UI";
    font-size: 10px;
    padding: 8px;
}

/* ===== 滑块样式 ===== */
QSlider::groove:horizontal {
    background: rgba(50, 50, 50, 0.8);
    border: 1px solid #555555;
    height: 6px;
    border-radius: 3px;
}

QSlider::sub-page:horizontal {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                               stop:0 #808080, stop:1 #606060);
    border-radius: 3px;
}

QSlider::handle:horizontal {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                               stop:0 #e0e0e0, stop:0.5 #c0c0c0, stop:1 #e0e0e0);
    border: 1px solid #666666;
    width: 14px;
    border-radius: 7px;
    margin: -4px 0;
}

QSlider::handle:horizontal:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                               stop:0 #ffffff, stop:0.5 #e0e0e0, stop:1 #ffffff);
    border: 1px solid #888888;
}

/* ===== 进度条滑块特殊样式 ===== */
QSlider#progressSlider::sub-page:horizontal {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                               stop:0 #909090, stop:1 #707070);
}

/* ===== 音量滑块特殊样式 ===== */
QSlider#volumeSlider::sub-page:horizontal {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                               stop:0 #a0a0a0, stop:1 #808080);
}

/* ===== 菜单栏和状态栏 ===== */
QMenuBar {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                               stop:0 #404040, stop:1 #303030);
    border-bottom: 1px solid #555555;
    color: #e0e0e0;
    font-family: "Microsoft YaHei UI", "Segoe UI";
}

QStatusBar {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                               stop:0 #303030, stop:1 #202020);
    color: #888888;
    font-family: "Microsoft YaHei UI", "Segoe UI";
    font-size: 10px;
    border-top: 1px solid #555555;
}

/* ===== 滚动条样式 ===== */
QScrollBar:vertical {
    background: rgba(40, 40, 40, 0.8);
    width: 12px;
    border-radius: 6px;
}

QScrollBar::handle:vertical {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                               stop:0 #606060, stop:0.5 #707070, stop:1 #606060);
    border-radius: 6px;
    min-height: 20px;
}

QScrollBar::handle:vertical:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                               stop:0 #707070, stop:0.5 #808080, stop:1 #707070);
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    border: none;
    background: none;
}

/* ===== 消息框样式 ===== */
QMessageBox {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                               stop:0 #1a1a1a, stop:0.5 #2a2a2a, stop:1 #1a1a1a);
    color: #e0e0e0;
}

QMessageBox QLabel {
    background: transparent;
    color: #e0e0e0;
    font-family: "Microsoft YaHei UI", "Segoe UI";
    font-size: 12px;
    border: none;
    background-color: transparent;
}

QMessageBox QPushButton {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                               stop:0 #404040, stop:0.5 #303030, stop:1 #404040);
    border: 1px solid #666666;
    border-radius: 6px;
    color: #e0e0e0;
    font-family: "Microsoft YaHei UI", "Segoe UI";
    font-size: 11px;
    font-weight: bold;
    padding: 8px 16px;
    min-width: 70px;
}

QMessageBox QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                               stop:0 #505050, stop:0.5 #404040, stop:1 #505050);
    border: 1px solid #888888;
    color: #ffffff;
}

QMessageBox QPushButton:pressed {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                               stop:0 #303030, stop:0.5 #202020, stop:1 #303030);
    border: 1px solid #444444;
}

/* ===== 输入对话框样式 ===== */
QInputDialog {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                               stop:0 #1a1a1a, stop:0.5 #2a2a2a, stop:1 #1a1a1a);
    color: #e0e0e0;
}

QInputDialog QLabel {
    background: transparent;
    color: #e0e0e0;
    font-family: "Microsoft YaHei UI", "Segoe UI";
    font-size: 12px;
    border: none;
    background-color: transparent;
}

QInputDialog QLineEdit {
    background: rgba(30, 30, 30, 0.9);
    border: 1px solid #555555;
    border-radius: 6px;
    color: #e0e0e0;
    font-family: "Consolas", "Microsoft YaHei UI";
    font-size: 11px;
    padding: 8px 12px;
}

QInputDialog QPushButton {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                               stop:0 #404040, stop:0.5 #303030, stop:1 #404040);
    border: 1px solid #666666;
    border-radius: 6px;
    color: #e0e0e0;
    font-family: "Microsoft YaHei UI", "Segoe UI";
    font-size: 11px;
    font-weight: bold;
    padding: 8px 16px;
    min-width: 70px;
}

QInputDialog QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                               stop:0 #505050, stop:0.5 #404040, stop:1 #505050);
    border: 1px solid #888888;
    color: #ffffff;
}

/* ===== 文件对话框样式 ===== */
QFileDialog {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                               stop:0 #1a1a1a, stop:0.5 #2a2a2a, stop:1 #1a1a1a);
    color: #e0e0e0;
}

QFileDialog QLabel {
    background: transparent;
    color: #e0e0e0;
    font-family: "Microsoft YaHei UI", "Segoe UI";
    font-size: 12px;
    border: none;
    background-color: transparent;
}

QFileDialog QTreeView, QFileDialog QListView {
    background: rgba(25, 25, 25, 0.9);
    border: 1px solid #555555;
    border-radius: 6px;
    color: #e0e0e0;
    font-family: "Microsoft YaHei UI", "Segoe UI";
    font-size: 11px;
    outline: none;
}

QFileDialog QLineEdit {
    background: rgba(30, 30, 30, 0.9);
    border: 1px solid #555555;
    border-radius: 6px;
    color: #e0e0e0;
    font-family: "Consolas", "Microsoft YaHei UI";
    font-size: 11px;
    padding: 8px 12px;
}

QFileDialog QPushButton {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                               stop:0 #404040, stop:0.5 #303030, stop:1 #404040);
    border: 1px solid #666666;
    border-radius: 6px;
    color: #e0e0e0;
    font-family: "Microsoft YaHei UI", "Segoe UI";
    font-size: 11px;
    font-weight: bold;
    padding: 8px 16px;
    min-width: 70px;
}

QFileDialog QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                               stop:0 #505050, stop:0.5 #404040, stop:1 #505050);
    border: 1px solid #888888;
    color: #ffffff;
}

/* ===== 布局间距调整 ===== */
QVBoxLayout, QHBoxLayout {
    spacing: 8px;
    margin: 5px;
}
"""