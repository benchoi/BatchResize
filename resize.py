#!/usr/bin/python

import os, sys

from PyQt4.QtGui import *
from resize_qt import *

def listAllFiles(path):
    if path.endswith(os.sep):
        path = path[:-1]
    all_files = []
    for entry in os.listdir(path):
        subpath = path + os.sep + entry
        if os.path.isdir(subpath):
            all_files.extend(listAllFiles(subpath))
        else:
            all_files.append(subpath)
    return all_files

class ResizeDialog(QDialog):
    def __init__(self, app):
        super(ResizeDialog, self).__init__()

        self.app = app

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.addInputFolderButton.clicked.connect(self.addInputFolder)
        self.ui.removeInputFolderButton.clicked.connect(self.removeInputFolder)
        self.ui.chooseOutputFolderButton.clicked.connect(self.chooseOutputFolder)
        self.ui.resizeButton.clicked.connect(self.resizeImages)
        self.ui.cancelButton.clicked.connect(self.cancelResize)

        self.resizing = False

    def addInputFolder(self):
        input_dir = QFileDialog.getExistingDirectory()
        if len(input_dir) > 0:
            self.ui.inputFolders.addItem(input_dir)

    def removeInputFolder(self):
        cur_row = self.ui.inputFolders.currentRow()
        if cur_row != None:
            self.ui.inputFolders.takeItem(cur_row)

    def chooseOutputFolder(self):
        self.ui.outputFolder.setText(QFileDialog.getExistingDirectory())

    def resizeImages(self):
        output_path = str(self.ui.outputFolder.text())
        if output_path.endswith(os.sep):
            output_path = output_path[:-1]
        if not os.path.isdir(output_path):
            QMessageBox.critical(self, "Unable to proceed", "Select a valid output folder!")
            return
        if self.ui.inputFolders.count() == 0:
            QMessageBox.critical(self, "Unable to proceed", "No input folders specified!")
            return

        self.resizing = True
        self.ui.cancelButton.setEnabled(True)

        # Get folders in list
        paths = [str(self.ui.inputFolders.item(i).text()) for i in xrange(self.ui.inputFolders.count())]

        # Recursively list all images
        all_files = []
        for path in paths:
            all_files.extend(listAllFiles(path))

        # Resize
        (max_width, max_height) = (self.ui.maxWidth.value(), self.ui.maxHeight.value())
        self.ui.progressBar.setRange(0, len(all_files))
        used_filenames = dict()
        count = 0
        for input_file in all_files:
            filename = input_file[input_file.rfind(os.sep)+1:]
            if filename in used_filenames:
                used_filenames[filename] += 1
                ext_pos = filename.rfind(".")
                filename_without_ext = filename[:ext_pos]
                extension = filename[ext_pos:]
                filename = "%s-%d%s" % (filename_without_ext, used_filenames[filename], extension)
            else:
                used_filenames[filename] = 0
            output_file = output_path + os.sep + filename
            
            cmd = 'convert "%s" -resize %dx%d "%s"' % (input_file, max_width, max_height, output_file)
            os.system(cmd)
            count += 1
            self.ui.progressBar.setValue(count)

            # Ensure app stays responsive, check for cancel
            self.app.processEvents()
            if not self.resizing:
                return

        self.resizing = False
        self.ui.cancelButton.setEnabled(False)

    def cancelResize(self):
        self.resizing = False
        self.ui.cancelButton.setEnabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ResizeDialog(app)
    window.show()
    sys.exit(app.exec_())
