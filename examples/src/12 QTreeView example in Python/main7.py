from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMenu, QMenuBar, QTreeWidget, QLabel, QVBoxLayout, 
    QWidget, QStatusBar, QTextEdit, QDockWidget, QTreeWidgetItem
)
from PySide6.QtCore import Qt

class WellLogViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Well Log Viewer")
        
        self.setup_menus()
        self.setup_ui_components()
        self.setup_status_bar()

    def setup_menus(self):
        # Set up the main menu bar
        self.menu_bar = self.menuBar()
        self.file_menu = self.menu_bar.addMenu("File")
        self.edit_menu = self.menu_bar.addMenu("Edit")
        self.view_menu = self.menu_bar.addMenu("View")
        self.help_menu = self.menu_bar.addMenu("Help")
        self.processing_menu = self.menu_bar.addMenu("Processing Menu’s")

    def setup_ui_components(self):
        # Set up the tree widget in a dockable widget
        self.tree_dock_widget = QDockWidget("Company #1")
        self.tree_widget = QTreeWidget()
        self.tree_dock_widget.setWidget(self.tree_widget)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.tree_dock_widget)
        
        # Set up the information area
        self.info_text_edit = QTextEdit()
        self.info_text_edit.setReadOnly(True)
        self.info_dock_widget = QDockWidget("Information")
        self.info_dock_widget.setWidget(self.info_text_edit)
        self.addDockWidget(Qt.BottomDockWidgetArea, self.info_dock_widget)

        # Populate the tree widget with dummy data
        self.populate_tree_widget()

        # Placeholder for the log plot
        self.plot_label = QLabel("Log Plot Area - Placeholder for custom widget")
        self.setCentralWidget(self.plot_label)

    def populate_tree_widget(self):
        # Create root items
        well_log_root = QTreeWidgetItem(["Well Logs"])
        self.tree_widget.addTopLevelItem(well_log_root)
        
        # Add child items to root
        for well_name in ["Well #1", "Well #2"]:
            well_item = QTreeWidgetItem([well_name])
            well_log_root.addChild(well_item)
            for log_type in ["DTSM", "GR", "HCAL"]:
                log_item = QTreeWidgetItem([log_type])
                well_item.addChild(log_item)
        
        # Expand all items by default
        self.tree_widget.expandAll()

    def setup_status_bar(self):
        # Set up the status bar for messaging
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready")

# Main application setup
if __name__ == "__main__":
    app = QApplication([])
    main_window = WellLogViewer()
    main_window.show()
    app.exec()
