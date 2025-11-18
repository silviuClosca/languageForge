from __future__ import annotations

from typing import Callable, Optional

from aqt.qt import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox,
    QLabel,
    QCheckBox,
    Qt,
    QSpinBox,
)

from ..core.logic_settings import load_settings, save_settings, Settings


class SettingsView(QWidget):
    """Settings tab for FluencyForge.

    Exposes theme, visual, and startup/behavior options.
    """

    def __init__(
        self,
        parent: Optional[QWidget] = None,
        apply_theme_callback: Optional[Callable[[Settings], None]] = None,
    ) -> None:
        super().__init__(parent)

        self._apply_theme_callback = apply_theme_callback
        self._settings: Settings = load_settings()

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Visual section -----------------------------------------------
        visual_group = QGroupBox("Visual", self)
        visual_layout = QVBoxLayout(visual_group)

        # Font size spin box: user can type an exact point size within a range.
        font_row = QHBoxLayout()
        font_row.addWidget(QLabel("Font size (pt)", visual_group))
        self.font_spin = QSpinBox(visual_group)
        self.font_spin.setRange(8, 24)
        self.font_spin.setSingleStep(1)
        font_row.addWidget(self.font_spin, 0)

        visual_layout.addLayout(font_row)

        layout.addWidget(visual_group)

        # Startup / Behavior section -----------------------------------
        startup_group = QGroupBox("Startup / Behavior", self)
        startup_layout = QVBoxLayout(startup_group)

        self.open_on_startup_checkbox = QCheckBox(
            "Open FluencyForge automatically when Anki starts", startup_group
        )
        startup_layout.addWidget(self.open_on_startup_checkbox)

        layout.addWidget(startup_group)
        layout.addStretch(1)

        # Wire up initial values & signals
        self._load_into_widgets()
        self._connect_signals()

    # -----------------------------------------------------------------
    # Internal helpers
    # -----------------------------------------------------------------
    def _load_into_widgets(self) -> None:
        # Font size
        # New representation: a point size stored as a string (e.g. "11").
        raw = self._settings.font_size
        size = 11
        if isinstance(raw, str) and raw.isdigit():
            size = int(raw)
        elif isinstance(raw, str) and raw.startswith("scale_"):
            # Backward compatibility with slider-based scale values.
            try:
                scale = int(raw.split("_", 1)[1])
            except ValueError:
                scale = 0
            size = 11 + scale
        else:
            # Backward compatibility with old small/medium/large values.
            legacy_map = {"small": 10, "medium": 11, "large": 13}
            size = legacy_map.get(str(raw), 11)

        size = max(8, min(24, size))
        self.font_spin.setValue(size)

        # Startup
        self.open_on_startup_checkbox.setChecked(self._settings.open_on_startup)

    def _connect_signals(self) -> None:
        self.font_spin.valueChanged.connect(self._on_font_size_changed)
        self.open_on_startup_checkbox.toggled.connect(self._on_open_on_startup_toggled)

    def _on_font_size_changed(self, value: int) -> None:
        self._settings.font_size = str(int(value))
        save_settings(self._settings)
        self._apply_theme()

    def _on_open_on_startup_toggled(self, checked: bool) -> None:
        self._settings.open_on_startup = checked
        save_settings(self._settings)

    def _apply_theme(self) -> None:
        if self._apply_theme_callback is not None:
            self._apply_theme_callback(self._settings)
