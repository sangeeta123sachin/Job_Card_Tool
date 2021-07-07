import sys
from project2 import *
from retDataBasePythonFile import *
import pandas as pd
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import argparse


class abc(Ui_mainWindow):

    def __init__(self):
        super().__init__()
        self.app = QtGui.QApplication(sys.argv)
        self.MainWindow = QtGui.QMainWindow()
        super().setupUi(self.MainWindow)
        self.df1 = pd.DataFrame(
            {'job ID': ['1', '2'], 'Techno Layer': ['C028-ACT1', 'C028-ACT2'], 'Date': ['2020/04/17', '2020/04/18'],
             'GDS': ['thor_top_mask1', 'thor_top_mask2'], 'Brion version': ['r2015.12.00', 'r2016.12.00'],
             'Maskset': ['280MA', '280MB'], 'Block': ['P1-280MA', 'P2-280MA'], 'Product': ['thor_top _MASK', 'MASK_09'],
             'MRID': ['1014885', '1014886'],
             'job Type': ['PROD', 'PRO'], 'XOP route': ['C028_ENG_07', 'C028_ENG_08'],
             'OPC Package': ['13S-active', '12S-active'], 'Defects': ['144', '145'], 'Allready in RetBB': ['24', '25'],
             'Add in Retdb': ['120', '121'], 'Unknown': ['131', '132'], 'Accept': ['25', '26'], 'Hold': ['0', '1'],
             'Reject': ['0', '1'], 'Need Improvement': ['0', '1'], 'Detector': ['BRIDGE', 'BRIDGE'],
             'Subjob': ['2', '2'], 'Dose': ['+0.000', '-0.030'], 'Focus': ['+0.000', '-0.060'],
             'Bias': ['+0.000', '+0.000'], 'Worst': ['+48.760', '+37.920'], 'defects': ['37790', '37791'],
             'Category': ['No(Not_defined)', 'No(Not_defined)'], 'detector': ['BRIDGE', 'NECK'],
             'dose': ['-0.030', '+0.030'], 'focus': ['-0.060', '+0.060'], 'bias': ['+0.000', '+0.000'],
             'worst': ['+40.080', '+32.120'], 'KPI': ['0.935-------', '0.859------'], 'Alarm': ['No', 'Other'],
             'Categorized': ['def:663@subjob:0@844380@RATPROD@TFlexsx04202 Not_defined Unknown job844380_0345657',
                             ' def:374@subjob:0@844380@RATPROD']})

        i = 0

        parser = argparse.ArgumentParser()
        parser.add_argument('number1', help='first number')

        args = parser.parse_args()

        c = args.number1
        self.number2 = 0
        self.packageFilesTableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table_1.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table_2.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        for no in self.df1['job ID'].iteritems():

            if no[1] == c:
                self.number2 += 1
                self.jobIdLabel_2.setText(self.df1['job ID'][i])
                self.technoLayerLabel_2.setText(self.df1['Techno Layer'][i])
                self.dateLabel_2.setText(self.df1['Date'][i])
                self.gdsLabel_2.setText(self.df1['GDS'][i])
                self.brionVersionLabel_2.setText(self.df1['Brion version'][i])
                self.masksetLabel_2.setText(self.df1['Maskset'][i])
                self.blockLabel_2.setText(self.df1['Block'][i])
                self.productLabel_2.setText(self.df1['Product'][i])
                self.mridLabel_2.setText(self.df1['MRID'][i])
                self.jobTypeLabel_2.setText(self.df1['job Type'][i])
                self.xopRouteLabel_2.setText(self.df1['XOP route'][i])
                self.opcPackageLabel_2.setText(self.df1['OPC Package'][i])
                self.defectsLabel_2.setText(self.df1['Defects'][i])
                self.allreadyInRetDbLabel_2.setText(self.df1['Allready in RetBB'][i])
                self.addInRetDbLabel_2.setText(self.df1['Add in Retdb'][i])
                self.unknownLabel_2.setText(self.df1['Unknown'][i])
                self.acceptLabel_2.setText(self.df1['Accept'][i])
                self.holdLabel_2.setText(self.df1['Hold'][i])

                self.rejectLabel_2.setText(self.df1['Reject'][i])
                self.needImprovementLabel_2.setText(self.df1['Need Improvement'][i])

                self.header = self.table_1.horizontalHeader()
                self.header.setResizeMode(0, QtGui.QHeaderView.Stretch)
                self.header.setResizeMode(1, QtGui.QHeaderView.Stretch)
                self.header.setResizeMode(2, QtGui.QHeaderView.Stretch)
                self.header.setResizeMode(3, QtGui.QHeaderView.Stretch)
                self.header.setResizeMode(4, QtGui.QHeaderView.Stretch)
                self.header.setResizeMode(5, QtGui.QHeaderView.Stretch)

                self.rowPosition = self.table_1.rowCount()
                self.table_1.insertRow(self.rowPosition)
                self.table_1.setItem(self.rowPosition, 0, QtGui.QTableWidgetItem(self.df1['Detector'][i]))
                self.table_1.setItem(self.rowPosition, 1, QtGui.QTableWidgetItem(self.df1['Subjob'][i]))
                self.table_1.setItem(self.rowPosition, 2, QtGui.QTableWidgetItem(self.df1['Dose'][i]))
                self.table_1.setItem(self.rowPosition, 3, QtGui.QTableWidgetItem(self.df1['Focus'][i]))
                self.table_1.setItem(self.rowPosition, 4, QtGui.QTableWidgetItem(self.df1['Bias'][i]))
                self.table_1.setItem(self.rowPosition, 5, QtGui.QTableWidgetItem(self.df1['Worst'][i]))
                self.table_1.setItem(self.rowPosition, 6, QtGui.QTableWidgetItem(self.df1['defects'][i]))
                self.table_1.setItem(self.rowPosition, 7, QtGui.QTableWidgetItem(self.df1['Category'][i]))
                self.header = self.table_2.horizontalHeader()

                self.header.setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
                self.header.setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
                self.header.setResizeMode(2, QtGui.QHeaderView.ResizeToContents)
                self.header.setResizeMode(3, QtGui.QHeaderView.ResizeToContents)
                self.header.setResizeMode(4, QtGui.QHeaderView.ResizeToContents)
                self.header.setResizeMode(5, QtGui.QHeaderView.ResizeToContents)
                self.header.setResizeMode(6, QtGui.QHeaderView.ResizeToContents)
                self.header.setResizeMode(7, QtGui.QHeaderView.Stretch)

                self.rowPosition = self.table_2.rowCount()
                self.table_2.insertRow(self.rowPosition)

                self.table_2.setItem(self.rowPosition, 0, QtGui.QTableWidgetItem(self.df1['defects'][i]))
                self.table_2.setItem(self.rowPosition, 1, QtGui.QTableWidgetItem(self.df1['dose'][i]))
                self.table_2.setItem(self.rowPosition, 2, QtGui.QTableWidgetItem(self.df1['focus'][i]))
                self.table_2.setItem(self.rowPosition, 3, QtGui.QTableWidgetItem(self.df1['bias'][i]))
                self.table_2.setItem(self.rowPosition, 4, QtGui.QTableWidgetItem(self.df1['worst'][i]))
                self.table_2.setItem(self.rowPosition, 5, QtGui.QTableWidgetItem(self.df1['KPI'][i]))
                self.table_2.setItem(self.rowPosition, 6, QtGui.QTableWidgetItem(self.df1['Alarm'][i]))
                self.table_2.setItem(self.rowPosition, 7, QtGui.QTableWidgetItem(self.df1['Categorized'][i]))

            i += 1

        if self.number2 == 0:
            self.abc('Dialog Box', 'Gob Id is not present')

        self.MainWindow.show()
        self.jobDefectClassificationButton.clicked.connect(lambda: self.openGui())
        self.pushButton.clicked.connect(self.buttonClicked)
        sys.exit(self.app.exec_())

    def abc(self, title, message):
        msg = QMessageBox()
        msg.setText(message)
        msg.setWindowTitle(title)
        if QMessageBox.Ok:
            msg.close()

        msg.exec_()
        exit()

    def buttonClicked(self):
        exit()

    def openGui(self):
        self.newWindow = retDataBase()
        for i in range(15):
            self.rowPosition = self.newWindow.table_1.rowCount()
            self.newWindow.table_1.insertRow(self.rowPosition)
        self.header = self.newWindow.table_1.horizontalHeader()

        self.header.setResizeMode(0, QtGui.QHeaderView.Stretch)
        self.header.setResizeMode(1, QtGui.QHeaderView.Stretch)
        self.header.setResizeMode(2, QtGui.QHeaderView.Stretch)
        self.header.setResizeMode(3, QtGui.QHeaderView.Stretch)
        self.header.setResizeMode(4, QtGui.QHeaderView.Stretch)
        self.header.setResizeMode(5, QtGui.QHeaderView.Stretch)
        self.header.setResizeMode(6, QtGui.QHeaderView.Stretch)
        self.header.setResizeMode(7, QtGui.QHeaderView.Stretch)
        self.header.setResizeMode(8, QtGui.QHeaderView.Stretch)

        self.df2 = pd.DataFrame({'Value': ['34.5', '-23.48', '-20.16', '16.84', '14.28', '-12.49', '-12.35', '-9.15',
                                           '0.99', '1.84', '32.12', '46.85', '22.46', '22.34', '-23.90'], 'Occurence':
                                     ['4', '2', '2', '2', '2', '2', '2', '2', '4', '2', '2', '2', '4', '1', '1'],
                                 'Subjob': ['1', '1', '7', '7', '7', '4', '4', '7', '1', '3', '7', '4', '1', '1', '4'],
                                 'Detector': ['NECK', 'CONDIST', 'CONDIST',
                                              'CONDIST', 'CONDIST', 'CONDIST', 'NECK', 'IMINMAX', 'IMINMAX', 'IMINMAX',
                                              'IMINMAX', 'NECK', 'NECK', 'CONDIST', 'CONDIST'],
                                 'Dose FOcus Bias': ['(.03 -0.6 0)', '(0 0 0)', '(0 0 0)', '(0 0 0)',
                                                     '(0 0 0)', '(0 0 0)', '(0 0 0)', '(0 0 0)', '(0 0 0)',
                                                     '(.03 -0.6 0)', '(0 0 0)', '(0 0 0)', '(0 0 0)', '(0 0 0)',
                                                     '(0 0 0)'], 'Classification': ['Not_defined', 'Sub_DRM_structure',
                                                                                    'Input_Design_Error',
                                                                                    'False_defect', 'SRAM_Design',
                                                                                    'OPC_Field', 'Other', 'Other',
                                                                                    'SRAM_Design', 'OPC_Field',
                                                                                    'False_defect',
                                                                                    'Input_Design_Error',
                                                                                    'Sub_DRM_structure', 'Not_defined',
                                                                                    'Other'],
                                 'Ret Valid': ['Unknown', 'Accept', 'Hold', 'Reject', 'Need Improvement', 'Unknown',
                                               'Accept', 'Hold', 'Reject', 'Need Improvement', 'Unknown', 'Accept',
                                               'Hold', 'Reject',
                                               'Need Improvement'],
                                 'Ret Name': ['Neck', 'false_defect', 'SB_print_not_critical', 'Neck', 'false_defect',
                                              'SB_print_not_critical', 'Neck', 'False_defect', 'SB_print_not_critical',
                                              'Neck', 'false_defect', 'SB_print_not_critical', 'Neck', 'false_defect',
                                              'SB_print_not_critical'],
                                 'Classif Help': ['Inherited', 'Inherited', 'Inherited', 'Inherited', 'Inherited',
                                                  'Inherited', 'Inherited', 'Inherited', 'Inherited', 'Inherited',
                                                  'Inherited', 'Inherited', 'Inherited', 'Inherited', 'Inherited']})

        for j in range(len(self.df2)):
            self.newWindow.table_1.setItem(j, 0, QtGui.QTableWidgetItem(self.df2['Value'][j]))
            self.newWindow.table_1.setItem(j, 1, QtGui.QTableWidgetItem(self.df2['Occurence'][j]))
            self.newWindow.table_1.setItem(j, 2, QtGui.QTableWidgetItem(self.df2['Subjob'][j]))
            self.newWindow.table_1.setItem(j, 3, QtGui.QTableWidgetItem(self.df2['Detector'][j]))
            self.newWindow.table_1.setItem(j, 4, QtGui.QTableWidgetItem(self.df2['Dose FOcus Bias'][j]))
            self.newWindow.table_1.setItem(j, 5, QtGui.QTableWidgetItem(self.df2['Classification'][j]))
            self.newWindow.table_1.setItem(j, 6, QtGui.QTableWidgetItem(self.df2['Ret Valid'][j]))
            self.newWindow.table_1.setItem(j, 7, QtGui.QTableWidgetItem(self.df2['Ret Name'][j]))
            self.newWindow.table_1.setItem(j, 8, QtGui.QTableWidgetItem(self.df2['Classif Help'][j]))
            self.newWindow.label.setText(self.technoLayerLabel_2.text())
            self.newWindow.productLabel_2.setText(self.gdsLabel_2.text())
            self.newWindow.dateLabel_2.setText(self.dateLabel_2.text())
            self.newWindow.label_6.setText(self.opcPackageLabel_2.text())
            self.newWindow.table_1.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

        self.newWindow.childWindow.show()
        self.l = []
        self.list_2 = []

        self.newWindow.unknownCheckBox.clicked.connect(lambda: self.btnClicked(self.newWindow.unknownCheckBox))
        self.newWindow.acceptCheckBox.clicked.connect(lambda: self.btnClicked(self.newWindow.acceptCheckBox))
        self.newWindow.holdCheckBox.clicked.connect(lambda: self.btnClicked(self.newWindow.holdCheckBox))
        self.newWindow.rejectCheckBox.clicked.connect(lambda: self.btnClicked(self.newWindow.rejectCheckBox))
        self.newWindow.needImprovementCheckBox.clicked.connect(
            lambda: self.btnClicked(self.newWindow.needImprovementCheckBox))
        self.newWindow.notDefinedCheckBox.clicked.connect(
            lambda: self.categoryButton(self.newWindow.notDefinedCheckBox))
        self.newWindow.subDrmStructureCheckBox.clicked.connect(
            lambda: self.categoryButton(self.newWindow.subDrmStructureCheckBox))
        self.newWindow.inputDesignErrorCheckBox.clicked.connect(
            lambda: self.categoryButton(self.newWindow.inputDesignErrorCheckBox))
        self.newWindow.falseDefectCheckBox.clicked.connect(
            lambda: self.categoryButton(self.newWindow.falseDefectCheckBox))
        self.newWindow.sramDesignCheckBox.clicked.connect(
            lambda: self.categoryButton(self.newWindow.sramDesignCheckBox))
        self.newWindow.opcFieldCheckBox.clicked.connect(lambda: self.categoryButton(self.newWindow.opcFieldCheckBox))
        self.newWindow.otherCheckBox.clicked.connect(lambda: self.categoryButton(self.newWindow.otherCheckBox))
        self.newWindow.occurrenceRadioButton.clicked.connect(
            lambda: self.sortValues(self.newWindow.occurrenceRadioButton, 1))
        self.newWindow.subjobRadioButton.clicked.connect(lambda: self.sortValues(self.newWindow.subjobRadioButton, 2))
        self.newWindow.retNameRadioButton.clicked.connect(lambda: self.sortValues(self.newWindow.retNameRadioButton, 7))
        self.newWindow.detectorRadioButton.clicked.connect(
            lambda: self.sortValues(self.newWindow.detectorRadioButton, 3))
        self.newWindow.dosefocusbiasRadioButton.clicked.connect(
            lambda: self.sortValues(self.newWindow.dosefocusbiasRadioButton, 4))

    def btnClicked(self, a):

        self.p = []

        if a.isChecked():
            for j in range(len(self.df2)):
                self.newWindow.table_1.setItem(j, 6, QtGui.QTableWidgetItem(self.df2['Ret Valid'][j]))
            self.l.append(a.text())

            items_3 = []
            for m in range(len(self.l)):
                items = self.newWindow.table_1.findItems(self.l[m], QtCore.Qt.MatchExactly)
                items_3.append(items)

            for x in range(len(items_3)):
                for y in range(len(items_3[x])):
                    self.p.append(items_3[x][y].text())
            if items_3:
                for j in range(15):
                    self.newWindow.table_1.setItem(j, 6, QtGui.QTableWidgetItem(''))
                for k in range(len(self.p)):
                    self.newWindow.table_1.setItem(k, 6, QtGui.QTableWidgetItem(self.p[k]))


        else:
            self.u = []
            for i in range(15):
                self.newWindow.table_1.setItem(i, 6, QtGui.QTableWidgetItem(self.df2['Ret Valid'][i]))
            self.l.remove(a.text())

            items_2 = []
            for m in range(len(self.l)):
                items_1 = self.newWindow.table_1.findItems(self.l[m], QtCore.Qt.MatchExactly)
                items_2.append(items_1)

            for x in range(len(items_2)):
                for y in range(len(items_2[x])):
                    self.u.append(items_2[x][y].text())
            if items_2:
                for j in range(len(self.df2)):
                    self.newWindow.table_1.setItem(j, 6, QtGui.QTableWidgetItem(''))
                for k in range(len(self.u)):
                    self.newWindow.table_1.setItem(k, 6, QtGui.QTableWidgetItem(self.u[k]))

    def categoryButton(self, button_2):

        self.m = []

        if button_2.isChecked():
            for j in range(len(self.df2)):
                self.newWindow.table_1.setItem(j, 5, QtGui.QTableWidgetItem(self.df2['Classification'][j]))
            self.list_2.append(button_2.text())

            items_5 = []
            for m in range(len(self.list_2)):
                items_4 = self.newWindow.table_1.findItems(self.list_2[m], QtCore.Qt.MatchExactly)
                items_5.append(items_4)

            for x in range(len(items_5)):
                for y in range(len(items_5[x])):
                    self.m.append(items_5[x][y].text())
            if items_5:
                for j in range(len(self.df2)):
                    self.newWindow.table_1.setItem(j, 5, QtGui.QTableWidgetItem(''))
                for k in range(len(self.m)):
                    self.newWindow.table_1.setItem(k, 5, QtGui.QTableWidgetItem(self.m[k]))


        else:
            self.n = []
            for i in range(len(self.df2)):
                self.newWindow.table_1.setItem(i, 5, QtGui.QTableWidgetItem(self.df2['Classification'][i]))
            self.list_2.remove(button_2.text())

            items_6 = []
            for m in range(len(self.list_2)):
                items_1 = self.newWindow.table_1.findItems(self.list_2[m], QtCore.Qt.MatchExactly)
                items_6.append(items_1)

            for x in range(len(items_6)):
                for y in range(len(items_6[x])):
                    self.n.append(items_6[x][y].text())
            if items_6:
                for j in range(15):
                    self.newWindow.table_1.setItem(j, 5, QtGui.QTableWidgetItem(''))
                for k in range(len(self.n)):
                    self.newWindow.table_1.setItem(k, 5, QtGui.QTableWidgetItem(self.n[k]))

    def sortValues(self, radioButton, col):

        listOfValues = []
        if radioButton.isChecked():
            for i in range(len(self.df2)):
                values = self.newWindow.table_1.takeItem(i, col)
                listOfValues.append(values.text())
            listOfValues.sort(reverse=True)

            for j in range(len(self.df2)):
                self.newWindow.table_1.setItem(j, col, QtGui.QTableWidgetItem(listOfValues[j]))

        if self.newWindow.occurrenceRadioButton.isChecked() == False:
            for k in range(len(self.df2)):
                self.newWindow.table_1.setItem(k, 1, QtGui.QTableWidgetItem(self.df2['Occurence'][k]))
        if self.newWindow.retNameRadioButton.isChecked() == False:
            for k in range(len(self.df2)):
                self.newWindow.table_1.setItem(k, 7, QtGui.QTableWidgetItem(self.df2['Ret Name'][k]))
        if self.newWindow.detectorRadioButton.isChecked() == False:
            for k in range(len(self.df2)):
                self.newWindow.table_1.setItem(k, 3, QtGui.QTableWidgetItem(self.df2['Detector'][k]))
        if self.newWindow.dosefocusbiasRadioButton.isChecked() == False:
            for k in range(len(self.df2)):
                self.newWindow.table_1.setItem(k, 4, QtGui.QTableWidgetItem(self.df2['Dose FOcus Bias'][k]))
        if self.newWindow.subjobRadioButton.isChecked() == False:
            for k in range(len(self.df2)):
                self.newWindow.table_1.setItem(k, 2, QtGui.QTableWidgetItem(self.df2['Subjob'][k]))


if __name__ == '__main__':
    abc()








