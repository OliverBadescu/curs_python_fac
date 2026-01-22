from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class ChartWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.figure = Figure(figsize=(5, 4))
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

    def clear(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.text(0.5, 0.5, "No data", ha='center', va='center', fontsize=14)
        ax.axis('off')
        self.canvas.draw()

    def plot_pie(self, data: dict, title: str):
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        labels = list(data.keys())
        values = list(data.values())

        colors = ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40', '#C9CBCF']

        ax.pie(values, labels=labels, autopct='%1.1f%%', colors=colors[:len(labels)])
        ax.set_title(title)
        self.figure.tight_layout()
        self.canvas.draw()

    def plot_bar(self, data: dict, title: str):
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        months = list(data.keys())
        values = list(data.values())
        month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        labels = [month_names[m - 1] for m in months]

        bars = ax.bar(labels, values, color='#36A2EB')
        ax.set_xlabel('Month')
        ax.set_ylabel('Amount ($)')
        ax.set_title(title)

        for bar, val in zip(bars, values):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                    f'${val:.0f}', ha='center', va='bottom', fontsize=8)

        self.figure.tight_layout()
        self.canvas.draw()
