# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MetadataOptionsPage(object):
    def setupUi(self, MetadataOptionsPage):
        MetadataOptionsPage.setObjectName("MetadataOptionsPage")
        MetadataOptionsPage.resize(423, 553)
        self.verticalLayout = QtWidgets.QVBoxLayout(MetadataOptionsPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.metadata_groupbox = QtWidgets.QGroupBox(MetadataOptionsPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.metadata_groupbox.sizePolicy().hasHeightForWidth())
        self.metadata_groupbox.setSizePolicy(sizePolicy)
        self.metadata_groupbox.setMinimumSize(QtCore.QSize(397, 135))
        self.metadata_groupbox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.metadata_groupbox.setObjectName("metadata_groupbox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.metadata_groupbox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.translate_artist_names = QtWidgets.QCheckBox(self.metadata_groupbox)
        self.translate_artist_names.setObjectName("translate_artist_names")
        self.verticalLayout_3.addWidget(self.translate_artist_names)
        self.artist_locale = QtWidgets.QComboBox(self.metadata_groupbox)
        self.artist_locale.setObjectName("artist_locale")
        self.verticalLayout_3.addWidget(self.artist_locale)
        self.standardize_artists = QtWidgets.QCheckBox(self.metadata_groupbox)
        self.standardize_artists.setObjectName("standardize_artists")
        self.verticalLayout_3.addWidget(self.standardize_artists)
        self.use_instrument_credits = QtWidgets.QCheckBox(self.metadata_groupbox)
        self.use_instrument_credits.setObjectName("use_instrument_credits")
        self.verticalLayout_3.addWidget(self.use_instrument_credits)
        self.convert_punctuation = QtWidgets.QCheckBox(self.metadata_groupbox)
        self.convert_punctuation.setObjectName("convert_punctuation")
        self.verticalLayout_3.addWidget(self.convert_punctuation)
        self.release_ars = QtWidgets.QCheckBox(self.metadata_groupbox)
        self.release_ars.setObjectName("release_ars")
        self.verticalLayout_3.addWidget(self.release_ars)
        self.track_ars = QtWidgets.QCheckBox(self.metadata_groupbox)
        self.track_ars.setObjectName("track_ars")
        self.verticalLayout_3.addWidget(self.track_ars)
        self.folksonomy_tags = QtWidgets.QCheckBox(self.metadata_groupbox)
        self.folksonomy_tags.setObjectName("folksonomy_tags")
        self.verticalLayout_3.addWidget(self.folksonomy_tags)
        self.verticalLayout.addWidget(self.metadata_groupbox)
        self.custom_fields_groupbox = QtWidgets.QGroupBox(MetadataOptionsPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.custom_fields_groupbox.sizePolicy().hasHeightForWidth())
        self.custom_fields_groupbox.setSizePolicy(sizePolicy)
        self.custom_fields_groupbox.setMinimumSize(QtCore.QSize(397, 0))
        self.custom_fields_groupbox.setObjectName("custom_fields_groupbox")
        self.gridlayout = QtWidgets.QGridLayout(self.custom_fields_groupbox)
        self.gridlayout.setSpacing(2)
        self.gridlayout.setObjectName("gridlayout")
        self.label_6 = QtWidgets.QLabel(self.custom_fields_groupbox)
        self.label_6.setObjectName("label_6")
        self.gridlayout.addWidget(self.label_6, 0, 0, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.custom_fields_groupbox)
        self.label_7.setObjectName("label_7")
        self.gridlayout.addWidget(self.label_7, 2, 0, 1, 2)
        self.nat_name = QtWidgets.QLineEdit(self.custom_fields_groupbox)
        self.nat_name.setObjectName("nat_name")
        self.gridlayout.addWidget(self.nat_name, 3, 0, 1, 1)
        self.nat_name_default = QtWidgets.QPushButton(self.custom_fields_groupbox)
        self.nat_name_default.setObjectName("nat_name_default")
        self.gridlayout.addWidget(self.nat_name_default, 3, 1, 1, 1)
        self.va_name_default = QtWidgets.QPushButton(self.custom_fields_groupbox)
        self.va_name_default.setObjectName("va_name_default")
        self.gridlayout.addWidget(self.va_name_default, 1, 1, 1, 1)
        self.va_name = QtWidgets.QLineEdit(self.custom_fields_groupbox)
        self.va_name.setObjectName("va_name")
        self.gridlayout.addWidget(self.va_name, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.custom_fields_groupbox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_6.setBuddy(self.va_name_default)
        self.label_7.setBuddy(self.nat_name_default)

        self.retranslateUi(MetadataOptionsPage)
        QtCore.QMetaObject.connectSlotsByName(MetadataOptionsPage)
        MetadataOptionsPage.setTabOrder(self.translate_artist_names, self.artist_locale)
        MetadataOptionsPage.setTabOrder(self.artist_locale, self.standardize_artists)
        MetadataOptionsPage.setTabOrder(self.standardize_artists, self.convert_punctuation)
        MetadataOptionsPage.setTabOrder(self.convert_punctuation, self.release_ars)
        MetadataOptionsPage.setTabOrder(self.release_ars, self.track_ars)
        MetadataOptionsPage.setTabOrder(self.track_ars, self.folksonomy_tags)
        MetadataOptionsPage.setTabOrder(self.folksonomy_tags, self.va_name)
        MetadataOptionsPage.setTabOrder(self.va_name, self.va_name_default)
        MetadataOptionsPage.setTabOrder(self.va_name_default, self.nat_name)
        MetadataOptionsPage.setTabOrder(self.nat_name, self.nat_name_default)

    def retranslateUi(self, MetadataOptionsPage):
        _translate = QtCore.QCoreApplication.translate
        self.metadata_groupbox.setTitle(_("Metadata"))
        self.translate_artist_names.setText(_("Translate artist names to this locale where possible:"))
        self.standardize_artists.setText(_("Use standardized artist names"))
        self.use_instrument_credits.setText(_("Use instrument and vocal credits"))
        self.convert_punctuation.setText(_("Convert Unicode punctuation characters to ASCII"))
        self.release_ars.setText(_("Use release relationships"))
        self.track_ars.setText(_("Use track relationships"))
        self.folksonomy_tags.setText(_("Use folksonomy tags as genre"))
        self.custom_fields_groupbox.setTitle(_("Custom Fields"))
        self.label_6.setText(_("Various artists:"))
        self.label_7.setText(_("Non-album tracks:"))
        self.nat_name_default.setText(_("Default"))
        self.va_name_default.setText(_("Default"))

