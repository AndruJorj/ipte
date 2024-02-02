#!/usr/bin/env python3


###############################
# MIT License

# Copyright (c) 2024 Andru Jorj

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
###############################


import curses

# Embedded data for elements
elements = [
    {'name': 'Hydrogen', 'symbol': 'H', 'atomic_number': 1, 'atomic_mass': 1.008, 'category': 'Nonmetal', 'electronegativity': 2.20},
    {'name': 'Helium', 'symbol': 'He', 'atomic_number': 2, 'atomic_mass': 4.0026, 'category': 'Noble gas', 'electronegativity': None},
    {'name': 'Lithium', 'symbol': 'Li', 'atomic_number': 3, 'atomic_mass': 6.94, 'category': 'Alkali Metal', 'electronegativity': 0.98},
    {'name': 'Beryllium', 'symbol': 'Be', 'atomic_number': 4, 'atomic_mass': 9.0122, 'category': 'Alkaline Earth', 'electronegativity': 1.57},
    {'name': 'Boron', 'symbol': 'B', 'atomic_number': 5, 'atomic_mass': 10.81, 'category': 'Metalloid', 'electronegativity': 2.04},
    {'name': 'Carbon', 'symbol': 'C', 'atomic_number': 6, 'atomic_mass': 12.011, 'category': 'Nonmetal', 'electronegativity': 2.55},
    {'name': 'Nitrogen', 'symbol': 'N', 'atomic_number': 7, 'atomic_mass': 14.007, 'category': 'Nonmetal', 'electronegativity': 3.04},
    {'name': 'Oxygen', 'symbol': 'O', 'atomic_number': 8, 'atomic_mass': 15.999, 'category': 'Nonmetal', 'electronegativity': 3.44},
    {'name': 'Fluorine', 'symbol': 'F', 'atomic_number': 9, 'atomic_mass': 18.998, 'category': 'Halogen', 'electronegativity': 3.98},
    {'name': 'Neon', 'symbol': 'Ne', 'atomic_number': 10, 'atomic_mass': 20.180, 'category': 'Noble gas', 'electronegativity': None},
    {'name': 'Sodium', 'symbol': 'Na', 'atomic_number': 11, 'atomic_mass': 22.990, 'category': 'Alkali Metal', 'electronegativity': 0.93},
    {'name': 'Magnesium', 'symbol': 'Mg', 'atomic_number': 12, 'atomic_mass': 24.305, 'category': 'Alkaline Earth', 'electronegativity': 1.31},
    {'name': 'Aluminum', 'symbol': 'Al', 'atomic_number': 13, 'atomic_mass': 26.982, 'category': 'Post-Trans.', 'electronegativity': 1.61},
    {'name': 'Silicon', 'symbol': 'Si', 'atomic_number': 14, 'atomic_mass': 28.085, 'category': 'Metalloid', 'electronegativity': 1.90},
    {'name': 'Phosphorus', 'symbol': 'P', 'atomic_number': 15, 'atomic_mass': 30.974, 'category': 'Nonmetal', 'electronegativity': 2.19},
    {'name': 'Sulfur', 'symbol': 'S', 'atomic_number': 16, 'atomic_mass': 32.06, 'category': 'Nonmetal', 'electronegativity': 2.58},
    {'name': 'Chlorine', 'symbol': 'Cl', 'atomic_number': 17, 'atomic_mass': 35.45, 'category': 'Halogen', 'electronegativity': 3.16},
    {'name': 'Argon', 'symbol': 'Ar', 'atomic_number': 18, 'atomic_mass': 39.948, 'category': 'Noble gas', 'electronegativity': None},
    {'name': 'Potassium', 'symbol': 'K', 'atomic_number': 19, 'atomic_mass': 39.098, 'category': 'Alkali Metal', 'electronegativity': 0.82},
    {'name': 'Calcium', 'symbol': 'Ca', 'atomic_number': 20, 'atomic_mass': 40.078, 'category': 'Alkaline Earth', 'electronegativity': 1.00},
    {'name': 'Scandium', 'symbol': 'Sc', 'atomic_number': 21, 'atomic_mass': 44.956, 'category': 'Transition Metal', 'electronegativity': 1.36},
    {'name': 'Titanium', 'symbol': 'Ti', 'atomic_number': 22, 'atomic_mass': 47.867, 'category': 'Transition Metal', 'electronegativity': 1.54},
    {'name': 'Vanadium', 'symbol': 'V', 'atomic_number': 23, 'atomic_mass': 50.942, 'category': 'Transition Metal', 'electronegativity': 1.63},
    {'name': 'Chromium', 'symbol': 'Cr', 'atomic_number': 24, 'atomic_mass': 51.996, 'category': 'Transition Metal', 'electronegativity': 1.66},
    {'name': 'Manganese', 'symbol': 'Mn', 'atomic_number': 25, 'atomic_mass': 54.938, 'category': 'Transition Metal', 'electronegativity': 1.55},
    {'name': 'Iron', 'symbol': 'Fe', 'atomic_number': 26, 'atomic_mass': 55.845, 'category': 'Transition Metal', 'electronegativity': 1.83},
    {'name': 'Nickel', 'symbol': 'Ni', 'atomic_number': 28, 'atomic_mass': 58.693, 'category': 'Transition Metal', 'electronegativity': 1.91},
    {'name': 'Copper', 'symbol': 'Cu', 'atomic_number': 29, 'atomic_mass': 63.546, 'category': 'Transition Metal', 'electronegativity': 1.90},
    {'name': 'Zinc', 'symbol': 'Zn', 'atomic_number': 30, 'atomic_mass': 65.380, 'category': 'Transition Metal', 'electronegativity': 1.65},
    {'name': 'Gallium', 'symbol': 'Ga', 'atomic_number': 31, 'atomic_mass': 69.723, 'category': 'Post-Trans.', 'electronegativity': 1.81},
    {'name': 'Germanium', 'symbol': 'Ge', 'atomic_number': 32, 'atomic_mass': 72.630, 'category': 'Metalloid', 'electronegativity': 2.01},
    {'name': 'Arsenic', 'symbol': 'As', 'atomic_number': 33, 'atomic_mass': 74.922, 'category': 'Metalloid', 'electronegativity': 2.18},
    {'name': 'Selenium', 'symbol': 'Se', 'atomic_number': 34, 'atomic_mass': 78.971, 'category': 'Nonmetal', 'electronegativity': 2.55},
    {'name': 'Bromine', 'symbol': 'Br', 'atomic_number': 35, 'atomic_mass': 79.904, 'category': 'Halogen', 'electronegativity': 2.96},
    {'name': 'Krypton', 'symbol': 'Kr', 'atomic_number': 36, 'atomic_mass': 83.798, 'category': 'Noble gas', 'electronegativity': None},
    {'name': 'Rubidium', 'symbol': 'Rb', 'atomic_number': 37, 'atomic_mass': 85.468, 'category': 'Alkali Metal', 'electronegativity': 0.82},
    {'name': 'Strontium', 'symbol': 'Sr', 'atomic_number': 38, 'atomic_mass': 87.620, 'category': 'Alkaline Earth', 'electronegativity': 0.95},
    {'name': 'Yttrium', 'symbol': 'Y', 'atomic_number': 39, 'atomic_mass': 88.906, 'category': 'Transition Metal', 'electronegativity': 1.22},
    {'name': 'Zirconium', 'symbol': 'Zr', 'atomic_number': 40, 'atomic_mass': 91.224, 'category': 'Transition Metal', 'electronegativity': 1.33},
    {'name': 'Niobium', 'symbol': 'Nb', 'atomic_number': 41, 'atomic_mass': 92.906, 'category': 'Transition Metal', 'electronegativity': 1.60},
    {'name': 'Molybdenum', 'symbol': 'Mo', 'atomic_number': 42, 'atomic_mass': 95.950, 'category': 'Transition Metal', 'electronegativity': 2.16},
    {'name': 'Technetium', 'symbol': 'Tc', 'atomic_number': 43, 'atomic_mass': None, 'category': 'Transition Metal', 'electronegativity': 1.90},
    {'name': 'Ruthenium', 'symbol': 'Ru', 'atomic_number': 44, 'atomic_mass': 101.070, 'category': 'Transition Metal', 'electronegativity': 2.20},
    {'name': 'Rhodium', 'symbol': 'Rh', 'atomic_number': 45, 'atomic_mass': 102.906, 'category': 'Transition Metal', 'electronegativity': 2.28},
    {'name': 'Palladium', 'symbol': 'Pd', 'atomic_number': 46, 'atomic_mass': 106.420, 'category': 'Transition Metal', 'electronegativity': 2.20},
    {'name': 'Silver', 'symbol': 'Ag', 'atomic_number': 47, 'atomic_mass': 107.868, 'category': 'Transition Metal', 'electronegativity': 1.93},
    {'name': 'Cadmium', 'symbol': 'Cd', 'atomic_number': 48, 'atomic_mass': 112.414, 'category': 'Transition Metal', 'electronegativity': 1.69},
    {'name': 'Indium', 'symbol': 'In', 'atomic_number': 49, 'atomic_mass': 114.818, 'category': 'Post-Trans.', 'electronegativity': 1.78},
    {'name': 'Tin', 'symbol': 'Sn', 'atomic_number': 50, 'atomic_mass': 118.710, 'category': 'Post-Trans.', 'electronegativity': 1.96},
    {'name': 'Antimony', 'symbol': 'Sb', 'atomic_number': 51, 'atomic_mass': 121.760, 'category': 'Metalloid', 'electronegativity': 2.05},
    {'name': 'Tellurium', 'symbol': 'Te', 'atomic_number': 52, 'atomic_mass': 127.600, 'category': 'Metalloid', 'electronegativity': 2.10},
    {'name': 'Iodine', 'symbol': 'I', 'atomic_number': 53, 'atomic_mass': 126.904, 'category': 'Halogen', 'electronegativity': 2.66},
    {'name': 'Xenon', 'symbol': 'Xe', 'atomic_number': 54, 'atomic_mass': 131.294, 'category': 'Noble gas', 'electronegativity': None},
    {'name': 'Cesium', 'symbol': 'Cs', 'atomic_number': 55, 'atomic_mass': 132.905, 'category': 'Alkali Metal', 'electronegativity': 0.79},
    {'name': 'Barium', 'symbol': 'Ba', 'atomic_number': 56, 'atomic_mass': 137.327, 'category': 'Alkaline Earth', 'electronegativity': 0.89},
    {'name': 'Lanthanum', 'symbol': 'La', 'atomic_number': 57, 'atomic_mass': 138.905, 'category': 'Lanthanide', 'electronegativity': 1.10},
    {'name': 'Cerium', 'symbol': 'Ce', 'atomic_number': 58, 'atomic_mass': 140.116, 'category': 'Lanthanide', 'electronegativity': 1.12},
    {'name': 'Praseodymium', 'symbol': 'Pr', 'atomic_number': 59, 'atomic_mass': 140.907, 'category': 'Lanthanide', 'electronegativity': 1.13},
    {'name': 'Neodymium', 'symbol': 'Nd', 'atomic_number': 60, 'atomic_mass': 144.242, 'category': 'Lanthanide', 'electronegativity': 1.14},
    {'name': 'Promethium', 'symbol': 'Pm', 'atomic_number': 61, 'atomic_mass': None, 'category': 'Lanthanide', 'electronegativity': 1.13},
    {'name': 'Samarium', 'symbol': 'Sm', 'atomic_number': 62, 'atomic_mass': 150.36, 'category': 'Lanthanide', 'electronegativity': 1.17},
    {'name': 'Europium', 'symbol': 'Eu', 'atomic_number': 63, 'atomic_mass': 151.966, 'category': 'Lanthanide', 'electronegativity': 1.20},
    {'name': 'Gadolinium', 'symbol': 'Gd', 'atomic_number': 64, 'atomic_mass': 157.25, 'category': 'Lanthanide', 'electronegativity': 1.20},
    {'name': 'Terbium', 'symbol': 'Tb', 'atomic_number': 65, 'atomic_mass': 158.925, 'category': 'Lanthanide', 'electronegativity': 1.20},
    {'name': 'Dysprosium', 'symbol': 'Dy', 'atomic_number': 66, 'atomic_mass': 162.500, 'category': 'Lanthanide', 'electronegativity': 1.22},
    {'name': 'Holmium', 'symbol': 'Ho', 'atomic_number': 67, 'atomic_mass': 164.930, 'category': 'Lanthanide', 'electronegativity': 1.23},
    {'name': 'Erbium', 'symbol': 'Er', 'atomic_number': 68, 'atomic_mass': 167.259, 'category': 'Lanthanide', 'electronegativity': 1.24},
    {'name': 'Thulium', 'symbol': 'Tm', 'atomic_number': 69, 'atomic_mass': 168.934, 'category': 'Lanthanide', 'electronegativity': 1.25},
    {'name': 'Ytterbium', 'symbol': 'Yb', 'atomic_number': 70, 'atomic_mass': 173.045, 'category': 'Lanthanide', 'electronegativity': 1.10},
    {'name': 'Lutetium', 'symbol': 'Lu', 'atomic_number': 71, 'atomic_mass': 174.966, 'category': 'Lanthanide', 'electronegativity': 1.27},
    {'name': 'Hafnium', 'symbol': 'Hf', 'atomic_number': 72, 'atomic_mass': 178.49, 'category': 'Transition Metal', 'electronegativity': 1.30},
    {'name': 'Tantalum', 'symbol': 'Ta', 'atomic_number': 73, 'atomic_mass': 180.947, 'category': 'Transition Metal', 'electronegativity': 1.50},
    {'name': 'Tungsten', 'symbol': 'W', 'atomic_number': 74, 'atomic_mass': 183.84, 'category': 'Transition Metal', 'electronegativity': 2.36},
    {'name': 'Rhenium', 'symbol': 'Re', 'atomic_number': 75, 'atomic_mass': 186.207, 'category': 'Transition Metal', 'electronegativity': 1.90},
    {'name': 'Osmium', 'symbol': 'Os', 'atomic_number': 76, 'atomic_mass': 190.23, 'category': 'Transition Metal', 'electronegativity': 2.20},
    {'name': 'Iridium', 'symbol': 'Ir', 'atomic_number': 77, 'atomic_mass': 192.217, 'category': 'Transition Metal', 'electronegativity': 2.20},
    {'name': 'Platinum', 'symbol': 'Pt', 'atomic_number': 78, 'atomic_mass': 195.084, 'category': 'Transition Metal', 'electronegativity': 2.28},
    {'name': 'Gold', 'symbol': 'Au', 'atomic_number': 79, 'atomic_mass': 196.967, 'category': 'Transition Metal', 'electronegativity': 2.54},
    {'name': 'Mercury', 'symbol': 'Hg', 'atomic_number': 80, 'atomic_mass': 200.592, 'category': 'Transition Metal', 'electronegativity': 2.00},
    {'name': 'Thallium', 'symbol': 'Tl', 'atomic_number': 81, 'atomic_mass': 204.38, 'category': 'Post-Trans.', 'electronegativity': 1.62},
    {'name': 'Lead', 'symbol': 'Pb', 'atomic_number': 82, 'atomic_mass': 207.2, 'category': 'Post-Trans.', 'electronegativity': 2.33},
    {'name': 'Bismuth', 'symbol': 'Bi', 'atomic_number': 83, 'atomic_mass': 208.98, 'category': 'Post-Trans.', 'electronegativity': 2.02},
    {'name': 'Polonium', 'symbol': 'Po', 'atomic_number': 84, 'atomic_mass': None, 'category': 'Metalloid', 'electronegativity': 2.0},
    {'name': 'Astatine', 'symbol': 'At', 'atomic_number': 85, 'atomic_mass': None, 'category': 'Halogen', 'electronegativity': 2.2},
    {'name': 'Radon', 'symbol': 'Rn', 'atomic_number': 86, 'atomic_mass': None, 'category': 'Noble gas', 'electronegativity': None},
    {'name': 'Francium', 'symbol': 'Fr', 'atomic_number': 87, 'atomic_mass': None, 'category': 'Alkali Metal', 'electronegativity': 0.7},
    {'name': 'Radium', 'symbol': 'Ra', 'atomic_number': 88, 'atomic_mass': None, 'category': 'Alkaline Earth', 'electronegativity': 0.9},
    {'name': 'Actinium', 'symbol': 'Ac', 'atomic_number': 89, 'atomic_mass': None, 'category': 'Actinide', 'electronegativity': 1.1},
    {'name': 'Thorium', 'symbol': 'Th', 'atomic_number': 90, 'atomic_mass': 232.037, 'category': 'Actinide', 'electronegativity': 1.3},
    {'name': 'Protactinium', 'symbol': 'Pa', 'atomic_number': 91, 'atomic_mass': 231.036, 'category': 'Actinide', 'electronegativity': 1.5},
    {'name': 'Uranium', 'symbol': 'U', 'atomic_number': 92, 'atomic_mass': 238.028, 'category': 'Actinide', 'electronegativity': 1.38},
    {'name': 'Neptunium', 'symbol': 'Np', 'atomic_number': 93, 'atomic_mass': None, 'category': 'Actinide', 'electronegativity': 1.36},
    {'name': 'Plutonium', 'symbol': 'Pu', 'atomic_number': 94, 'atomic_mass': None, 'category': 'Actinide', 'electronegativity': 1.28},
    {'name': 'Americium', 'symbol': 'Am', 'atomic_number': 95, 'atomic_mass': None, 'category': 'Actinide', 'electronegativity': 1.13},
    {'name': 'Curium', 'symbol': 'Cm', 'atomic_number': 96, 'atomic_mass': None, 'category': 'Actinide', 'electronegativity': 1.28},
    {'name': 'Berkelium', 'symbol': 'Bk', 'atomic_number': 97, 'atomic_mass': None, 'category': 'Actinide', 'electronegativity': 1.3},
    {'name': 'Californium', 'symbol': 'Cf', 'atomic_number': 98, 'atomic_mass': None, 'category': 'Actinide', 'electronegativity': 1.3},
    {'name': 'Einsteinium', 'symbol': 'Es', 'atomic_number': 99, 'atomic_mass': None, 'category': 'Actinide', 'electronegativity': 1.3},
    {'name': 'Fermium', 'symbol': 'Fm', 'atomic_number': 100, 'atomic_mass': None, 'category': 'Actinide', 'electronegativity': 1.3},
    {'name': 'Mendelevium', 'symbol': 'Md', 'atomic_number': 101, 'atomic_mass': None, 'category': 'Actinide', 'electronegativity': 1.3},
    {'name': 'Nobelium', 'symbol': 'No', 'atomic_number': 102, 'atomic_mass': None, 'category': 'Actinide', 'electronegativity': 1.3},
    {'name': 'Lawrencium', 'symbol': 'Lr', 'atomic_number': 103, 'atomic_mass': None, 'category': 'Actinide', 'electronegativity': 1.3},
    {'name': 'Rutherfordium', 'symbol': 'Rf', 'atomic_number': 104, 'atomic_mass': None, 'category': 'Transition Metal', 'electronegativity': 1.3},
    {'name': 'Dubnium', 'symbol': 'Db', 'atomic_number': 105, 'atomic_mass': None, 'category': 'Transition Metal', 'electronegativity': 1.3},
    {'name': 'Seaborgium', 'symbol': 'Sg', 'atomic_number': 106, 'atomic_mass': None, 'category': 'Transition Metal', 'electronegativity': 1.3},
    {'name': 'Bohrium', 'symbol': 'Bh', 'atomic_number': 107, 'atomic_mass': None, 'category': 'Transition Metal', 'electronegativity': 1.3},
    {'name': 'Hassium', 'symbol': 'Hs', 'atomic_number': 108, 'atomic_mass': None, 'category': 'Transition Metal', 'electronegativity': 1.3},
    {'name': 'Meitnerium', 'symbol': 'Mt', 'atomic_number': 109, 'atomic_mass': None, 'category': 'Transition Metal', 'electronegativity': 1.3},
    {'name': 'Darmstadtium', 'symbol': 'Ds', 'atomic_number': 110, 'atomic_mass': None, 'category': 'Transition Metal', 'electronegativity': 1.3},
    {'name': 'Roentgenium', 'symbol': 'Rg', 'atomic_number': 111, 'atomic_mass': None, 'category': 'Transition Metal', 'electronegativity': 1.3},
    {'name': 'Copernicium', 'symbol': 'Cn', 'atomic_number': 112, 'atomic_mass': None, 'category': 'Transition Metal', 'electronegativity': 1.3},
    {'name': 'Nihonium', 'symbol': 'Nh', 'atomic_number': 113, 'atomic_mass': None, 'category': 'Post-Trans.', 'electronegativity': 1.3},
    {'name': 'Flerovium', 'symbol': 'Fl', 'atomic_number': 114, 'atomic_mass': None, 'category': 'Post-Trans.', 'electronegativity': 1.3},
    {'name': 'Moscovium', 'symbol': 'Mc', 'atomic_number': 115, 'atomic_mass': None, 'category': 'Post-Trans.', 'electronegativity': 1.3},
    {'name': 'Livermorium', 'symbol': 'Lv', 'atomic_number': 116, 'atomic_mass': None, 'category': 'Post-Trans.', 'electronegativity': 1.3},
    {'name': 'Tennessine', 'symbol': 'Ts', 'atomic_number': 117, 'atomic_mass': None, 'category': 'Post-Trans.', 'electronegativity': 1.3},
    {'name': 'Oganesson', 'symbol': 'Og', 'atomic_number': 118, 'atomic_mass': None, 'category': 'Noble gas', 'electronegativity': None}
]

def display_element_info(stdscr, element):
    stdscr.clear()
    
    stdscr.addstr(1, 1, f"Element:", curses.color_pair(1) | curses.COLOR_BLUE)
    stdscr.addstr(f" {element['name']}", curses.color_pair(3) | curses.COLOR_YELLOW)
    
    stdscr.addstr(3, 1, f"Symbol:", curses.color_pair(2) | curses.COLOR_CYAN)
    stdscr.addstr(f" {element['symbol']}")
    
    stdscr.addstr(4, 1, f"Atomic Number:", curses.color_pair(2) | curses.COLOR_CYAN)
    stdscr.addstr(f" {element['atomic_number']}")
    
    stdscr.addstr(5, 1, f"Atomic Mass:", curses.color_pair(2) | curses.COLOR_CYAN)
    stdscr.addstr(f" {element['atomic_mass']}")
    
    stdscr.addstr(6, 1, f"Category:", curses.color_pair(2) | curses.COLOR_CYAN)
    stdscr.addstr(f" {element['category']}")
    
    stdscr.addstr(7, 1, f"Electronegativity:", curses.color_pair(2) | curses.COLOR_CYAN)
    stdscr.addstr(f" {element['electronegativity'] or '-'}")
    
    stdscr.addstr(9, 1, f"Press any key to go back.")

    stdscr.refresh()
    stdscr.getch()


def draw_menu(stdscr, current_row, start_row=0):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    for i, element in enumerate(elements[start_row:start_row + h - 1]):
        x = 1
        y = i + 1
        element_info = f"{element['atomic_number']:>3} {element['symbol']:<3} {element['name']}"
        lines = [element_info[i:i + w - 2] for i in range(0, len(element_info), w - 2)]

        for j, line in enumerate(lines):
            if len(line) < w - 2:
                padding = ' ' * (w - 2 - len(line))
                line += padding

            try:
                if i + start_row == current_row:
                    stdscr.addstr(y + j, x, line, curses.color_pair(1) | curses.A_BOLD)
                else:
                    stdscr.addstr(y + j, x, line)
            except curses.error as e:
                print(f"Error adding line for element {element['symbol']} at index {i}, line {j}: {e}")
                print(f"Problematic line: '{line}'")

    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    print_title(stdscr)
    current_row = 0
    start_row = 0

    while True:
        draw_menu(stdscr, current_row, start_row)
        key = stdscr.getch()

        if key == ord('q'):
            break
        elif key == curses.KEY_DOWN and current_row < len(elements) - 1:
            current_row += 1
            if current_row >= start_row + stdscr.getmaxyx()[0] - 1:
                start_row += 1
        elif key == curses.KEY_UP and current_row > 0:
            current_row -= 1
            if current_row < start_row:
                start_row -= 1
        elif key == ord('\n'):
            element = elements[current_row]
            display_element_info(stdscr, element)

def print_title(stdscr):
    title = "Interactive Periodic Table of Elements"
    title_attr = curses.color_pair(2)  # Assuming color pair 2 is used for the title

    height, width = stdscr.getmaxyx()
    title_row = 0
    title_col = (width - len(title)) // 2

    stdscr.addstr(title_row, title_col, title, title_attr)
    stdscr.refresh()


            
if __name__ == "__main__":
    curses.wrapper(main)
    
