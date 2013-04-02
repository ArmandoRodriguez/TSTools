# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_ccdctools.ui'
#
# Created: Tue Apr  2 05:40:25 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_CCDCTools(object):
    def setupUi(self, CCDCTools):
        CCDCTools.setObjectName(_fromUtf8("CCDCTools"))
        CCDCTools.resize(320, 320)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CCDCTools.sizePolicy().hasHeightForWidth())
        CCDCTools.setSizePolicy(sizePolicy)
        CCDCTools.setMinimumSize(QtCore.QSize(320, 320))
        self.verticalLayout_2 = QtGui.QVBoxLayout(CCDCTools)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(CCDCTools)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_options = QtGui.QWidget()
        self.tab_options.setObjectName(_fromUtf8("tab_options"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab_options)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.lab_band = QtGui.QLabel(self.tab_options)
        self.lab_band.setObjectName(_fromUtf8("lab_band"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lab_band)
        self.combox_band = QtGui.QComboBox(self.tab_options)
        self.combox_band.setObjectName(_fromUtf8("combox_band"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.combox_band)
        self.lab_min = QtGui.QLabel(self.tab_options)
        self.lab_min.setObjectName(_fromUtf8("lab_min"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.lab_min)
        self.lab_max = QtGui.QLabel(self.tab_options)
        self.lab_max.setObjectName(_fromUtf8("lab_max"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.lab_max)
        self.lab_fmask = QtGui.QLabel(self.tab_options)
        self.lab_fmask.setObjectName(_fromUtf8("lab_fmask"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.lab_fmask)
        self.cbox_fmask = QtGui.QCheckBox(self.tab_options)
        self.cbox_fmask.setObjectName(_fromUtf8("cbox_fmask"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.cbox_fmask)
        self.lab_fit = QtGui.QLabel(self.tab_options)
        self.lab_fit.setObjectName(_fromUtf8("lab_fit"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.lab_fit)
        self.cbox_ccdcfit = QtGui.QCheckBox(self.tab_options)
        self.cbox_ccdcfit.setObjectName(_fromUtf8("cbox_ccdcfit"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.cbox_ccdcfit)
        self.lab_breaks = QtGui.QLabel(self.tab_options)
        self.lab_breaks.setObjectName(_fromUtf8("lab_breaks"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.lab_breaks)
        self.cbox_ccdcbreak = QtGui.QCheckBox(self.tab_options)
        self.cbox_ccdcbreak.setObjectName(_fromUtf8("cbox_ccdcbreak"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.cbox_ccdcbreak)
        self.edit_min = QtGui.QLineEdit(self.tab_options)
        self.edit_min.setInputMask(_fromUtf8(""))
        self.edit_min.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.edit_min.setObjectName(_fromUtf8("edit_min"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.edit_min)
        self.edit_max = QtGui.QLineEdit(self.tab_options)
        self.edit_max.setInputMask(_fromUtf8(""))
        self.edit_max.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.edit_max.setObjectName(_fromUtf8("edit_max"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.edit_max)
        self.verticalLayout.addLayout(self.formLayout)
        self.tabWidget.addTab(self.tab_options, _fromUtf8(""))
        self.tab_images = QtGui.QWidget()
        self.tab_images.setObjectName(_fromUtf8("tab_images"))
        self.tabWidget.addTab(self.tab_images, _fromUtf8(""))
        self.tab_save = QtGui.QWidget()
        self.tab_save.setObjectName(_fromUtf8("tab_save"))
        self.tabWidget.addTab(self.tab_save, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)

        self.retranslateUi(CCDCTools)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CCDCTools)

    def retranslateUi(self, CCDCTools):
        CCDCTools.setWindowTitle(QtGui.QApplication.translate("CCDCTools", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.lab_band.setText(QtGui.QApplication.translate("CCDCTools", "Band", None, QtGui.QApplication.UnicodeUTF8))
        self.lab_min.setText(QtGui.QApplication.translate("CCDCTools", "Min", None, QtGui.QApplication.UnicodeUTF8))
        self.lab_max.setText(QtGui.QApplication.translate("CCDCTools", "Max", None, QtGui.QApplication.UnicodeUTF8))
        self.lab_fmask.setText(QtGui.QApplication.translate("CCDCTools", "Fmask", None, QtGui.QApplication.UnicodeUTF8))
        self.cbox_fmask.setText(QtGui.QApplication.translate("CCDCTools", "Show/Hide Fmask", None, QtGui.QApplication.UnicodeUTF8))
        self.lab_fit.setText(QtGui.QApplication.translate("CCDCTools", "CCDC Fit", None, QtGui.QApplication.UnicodeUTF8))
        self.cbox_ccdcfit.setText(QtGui.QApplication.translate("CCDCTools", "Show/Hide CCDC Fit", None, QtGui.QApplication.UnicodeUTF8))
        self.lab_breaks.setText(QtGui.QApplication.translate("CCDCTools", "CCDC Breaks", None, QtGui.QApplication.UnicodeUTF8))
        self.cbox_ccdcbreak.setText(QtGui.QApplication.translate("CCDCTools", "Show/Hide CCDC Breaks", None, QtGui.QApplication.UnicodeUTF8))
        self.edit_min.setText(QtGui.QApplication.translate("CCDCTools", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.edit_max.setText(QtGui.QApplication.translate("CCDCTools", "10000", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_options), QtGui.QApplication.translate("CCDCTools", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_images), QtGui.QApplication.translate("CCDCTools", "Images", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_save), QtGui.QApplication.translate("CCDCTools", "Save", None, QtGui.QApplication.UnicodeUTF8))

