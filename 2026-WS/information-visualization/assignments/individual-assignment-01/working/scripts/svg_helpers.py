"""Shared SVG marks and colours for the final assignment figures."""
from html import escape

INK, MUTED, TEAL, GRID = "#172b36", "#536572", "#087d80", "#dce3e7"


def text(x, y, content, size=24, color=INK, weight=400, anchor="start"):
    return (f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" '
            f'font-weight="{weight}" text-anchor="{anchor}">{escape(str(content))}</text>')


def line(x1, y1, x2, y2, color=GRID, width=2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"/>'


def circle(x, y, color, radius=8):
    return f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{color}"/>'
