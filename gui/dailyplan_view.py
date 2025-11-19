from __future__ import annotations

from typing import Optional

from aqt.qt import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QTextEdit,
    QPushButton,
    QCheckBox,
    Qt,
)

from ..core.logic_dailyplan import load_daily_plan, save_daily_plan
from ..core.models import DailyPlan


class DailyPlanView(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Task sections - generic labels for flexibility
        task_labels = ["Task 1", "Task 2", "Task 3", "Task 4"]
        self.task_edits = []
        
        for label in task_labels:
            layout.addWidget(QLabel(label, self))
            task_edit = QTextEdit(self)
            task_edit.setMaximumHeight(100)
            task_edit.textChanged.connect(self._on_save)
            layout.addWidget(task_edit)
            self.task_edits.append(task_edit)

        # Behavior: show on startup
        self.show_on_startup_checkbox = QCheckBox(
            "Open Today's Plan on startup", self
        )
        layout.addWidget(self.show_on_startup_checkbox)

        # Actions row
        actions_row = QHBoxLayout()
        actions_row.addStretch(1)
        self.save_button = QPushButton("Save Plan", self)
        actions_row.addWidget(self.save_button)
        layout.addLayout(actions_row)

        # Optional status label
        self.status_label = QLabel("", self)
        layout.addWidget(self.status_label)

        self.save_button.clicked.connect(self._on_save)

        self._load()

    def _load(self) -> None:
        plan: DailyPlan = load_daily_plan()
        # Load tasks into editors
        for i, task_edit in enumerate(self.task_edits):
            if i < len(plan.tasks):
                task_edit.setPlainText(plan.tasks[i] or "")
            else:
                task_edit.setPlainText("")
        self.show_on_startup_checkbox.setChecked(plan.show_on_startup)

    def _on_save(self) -> None:
        tasks = [edit.toPlainText() for edit in self.task_edits]
        plan = DailyPlan(
            tasks=tasks,
            show_on_startup=self.show_on_startup_checkbox.isChecked(),
        )
        save_daily_plan(plan)
        self.status_label.setText("Plan saved.")
