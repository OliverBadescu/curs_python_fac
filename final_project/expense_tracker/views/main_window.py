from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget,
    QLabel, QLineEdit, QComboBox, QPushButton, QDateEdit,
    QTableWidget, QTableWidgetItem, QHeaderView, QMessageBox,
    QSpinBox, QFrame
)
from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QDoubleValidator

from models.database import CATEGORIES
from views.charts import ChartWidget


class MainWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Expense Tracker")
        self.setMinimumSize(800, 600)

        self._setup_ui()
        self._refresh_expenses_table()

    def _setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        tabs = QTabWidget()
        tabs.addTab(self._create_add_tab(), "Add Expense")
        tabs.addTab(self._create_view_tab(), "View Expenses")
        tabs.addTab(self._create_summary_tab(), "Summary")
        layout.addWidget(tabs)

    def _create_add_tab(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setAlignment(Qt.AlignTop)

        form_frame = QFrame()
        form_layout = QVBoxLayout(form_frame)
        form_layout.setSpacing(15)

        # Amount
        amount_layout = QHBoxLayout()
        amount_layout.addWidget(QLabel("Amount ($):"))
        self.amount_input = QLineEdit()
        self.amount_input.setValidator(QDoubleValidator(0, 999999, 2))
        self.amount_input.setPlaceholderText("0.00")
        amount_layout.addWidget(self.amount_input)
        form_layout.addLayout(amount_layout)

        # Category
        category_layout = QHBoxLayout()
        category_layout.addWidget(QLabel("Category:"))
        self.category_input = QComboBox()
        self.category_input.addItems(CATEGORIES)
        category_layout.addWidget(self.category_input)
        form_layout.addLayout(category_layout)

        # Description
        desc_layout = QHBoxLayout()
        desc_layout.addWidget(QLabel("Description:"))
        self.description_input = QLineEdit()
        self.description_input.setPlaceholderText("Optional description")
        desc_layout.addWidget(self.description_input)
        form_layout.addLayout(desc_layout)

        # Date
        date_layout = QHBoxLayout()
        date_layout.addWidget(QLabel("Date:"))
        self.date_input = QDateEdit()
        self.date_input.setDate(QDate.currentDate())
        self.date_input.setCalendarPopup(True)
        date_layout.addWidget(self.date_input)
        form_layout.addLayout(date_layout)

        # Add button
        add_btn = QPushButton("Add Expense")
        add_btn.clicked.connect(self._on_add_expense)
        add_btn.setStyleSheet("padding: 10px; font-weight: bold;")
        form_layout.addWidget(add_btn)

        layout.addWidget(form_frame)
        layout.addStretch()
        return widget

    def _create_view_tab(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)

        # Table
        self.expenses_table = QTableWidget()
        self.expenses_table.setColumnCount(5)
        self.expenses_table.setHorizontalHeaderLabels(["ID", "Date", "Category", "Description", "Amount"])
        self.expenses_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.expenses_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.expenses_table.setEditTriggers(QTableWidget.NoEditTriggers)
        layout.addWidget(self.expenses_table)

        # Delete button
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        delete_btn = QPushButton("Delete Selected")
        delete_btn.clicked.connect(self._on_delete_expense)
        btn_layout.addWidget(delete_btn)
        refresh_btn = QPushButton("Refresh")
        refresh_btn.clicked.connect(self._refresh_expenses_table)
        btn_layout.addWidget(refresh_btn)
        layout.addLayout(btn_layout)

        return widget

    def _create_summary_tab(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)

        # Month/Year selector
        selector_layout = QHBoxLayout()
        selector_layout.addWidget(QLabel("Year:"))
        self.year_input = QSpinBox()
        self.year_input.setRange(2000, 2100)
        self.year_input.setValue(QDate.currentDate().year())
        selector_layout.addWidget(self.year_input)

        selector_layout.addWidget(QLabel("Month:"))
        self.month_input = QSpinBox()
        self.month_input.setRange(1, 12)
        self.month_input.setValue(QDate.currentDate().month())
        selector_layout.addWidget(self.month_input)

        update_btn = QPushButton("Update Charts")
        update_btn.clicked.connect(self._update_charts)
        selector_layout.addWidget(update_btn)
        selector_layout.addStretch()
        layout.addLayout(selector_layout)

        # Total label
        self.total_label = QLabel("Total: $0.00")
        self.total_label.setStyleSheet("font-size: 18px; font-weight: bold; margin: 10px;")
        layout.addWidget(self.total_label)

        # Charts
        charts_layout = QHBoxLayout()
        self.pie_chart = ChartWidget()
        self.bar_chart = ChartWidget()
        charts_layout.addWidget(self.pie_chart)
        charts_layout.addWidget(self.bar_chart)
        layout.addLayout(charts_layout)

        return widget

    def _on_add_expense(self):
        amount_text = self.amount_input.text()
        if not amount_text:
            QMessageBox.warning(self, "Error", "Please enter an amount")
            return

        try:
            amount = float(amount_text)
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid amount")
            return

        if amount <= 0:
            QMessageBox.warning(self, "Error", "Amount must be positive")
            return

        category = self.category_input.currentText()
        description = self.description_input.text()
        date = self.date_input.date().toString("yyyy-MM-dd")

        self.controller.add_expense(amount, category, description, date)

        # Clear form
        self.amount_input.clear()
        self.description_input.clear()
        self.date_input.setDate(QDate.currentDate())

        QMessageBox.information(self, "Success", "Expense added!")
        self._refresh_expenses_table()

    def _refresh_expenses_table(self):
        expenses = self.controller.get_all_expenses()
        self.expenses_table.setRowCount(len(expenses))

        for row, exp in enumerate(expenses):
            self.expenses_table.setItem(row, 0, QTableWidgetItem(str(exp.id)))
            self.expenses_table.setItem(row, 1, QTableWidgetItem(exp.date))
            self.expenses_table.setItem(row, 2, QTableWidgetItem(exp.category))
            self.expenses_table.setItem(row, 3, QTableWidgetItem(exp.description))
            self.expenses_table.setItem(row, 4, QTableWidgetItem(f"${exp.amount:.2f}"))

    def _on_delete_expense(self):
        selected = self.expenses_table.selectedItems()
        if not selected:
            QMessageBox.warning(self, "Error", "Please select an expense to delete")
            return

        row = selected[0].row()
        expense_id = int(self.expenses_table.item(row, 0).text())

        reply = QMessageBox.question(
            self, "Confirm", "Delete this expense?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            self.controller.delete_expense(expense_id)
            self._refresh_expenses_table()

    def _update_charts(self):
        year = self.year_input.value()
        month = self.month_input.value()

        # Update total
        category_totals = self.controller.get_category_totals(year, month)
        total = sum(category_totals.values())
        self.total_label.setText(f"Total for {month}/{year}: ${total:.2f}")

        # Update pie chart
        if category_totals:
            self.pie_chart.plot_pie(category_totals, f"Expenses by Category ({month}/{year})")
        else:
            self.pie_chart.clear()

        # Update bar chart
        monthly_totals = self.controller.get_monthly_totals(year)
        if monthly_totals:
            self.bar_chart.plot_bar(monthly_totals, f"Monthly Expenses ({year})")
        else:
            self.bar_chart.clear()
