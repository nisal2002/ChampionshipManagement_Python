# World Rally Cross Championship Management

This repository contains a Python command-line application for managing a World Rally Cross Championship. The system supports adding, deleting, updating driver details, viewing standings, simulating races, and saving/loading data.

## Features of the System

When launched, the system displays the following console menu:

- `ADD`: Add driver details
- `DDD`: Delete driver details
- `UDD`: Update driver details
- `VCT`: View the rally cross standings table
- `SRR`: Simulate a random race
- `VRL`: View race table sorted according to the date
- `STF`: Save the current data to a text file
- `RFF`: Load data from the saved text file
- `ESC`: Exit the program

## Functions

### Function 1: ADD

Allows the user to enter the following driver details:
- Name
- Age
- Team
- Car
- Current points

**Example:**
```plaintext
Travis Pastrana, 38, Subaru Motorsports, Subaru WRX STi, 10
```

### Function 2: DDD

Allows the user to delete a driver by searching by name.

### Function 3: UDD

Allows the user to update driver details by searching by name.

### Function 4: VCT

Displays the championship standings ordered by points in descending order. The table is formatted neatly with all details.

### Function 5: SRR

Simulates a random race and assigns points to each driver accordingly. Points are assigned as follows:
- 1st place: 10 points
- 2nd place: 7 points
- 3rd place: 5 points

Race details stored include:
- Date of the race
- Location of the race (Nyirád, Höljes, Montalegre, Barcelona, Rīga, Norway)
- Each driver’s position and points

### Function 6: VRL

Displays all races in the championship sorted according to the date using a custom algorithm.

### Function 7: STF

Saves the current data to a text file in a way that it can be retrieved easily. No database usage is allowed for storing data.

### Function 8: RFF

Loads the current data from the text file to enable resume capabilities.

## Project Structure

- **main.py**: The main Python file containing the implementation of the championship management system.

## How to Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/nisal2002/ChampionshipManagement_Python.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd ChampionshipManagement_Python
   ```

3. **Run the Python program:**

   ```bash
   python main.py
   ```

   The program will display a console menu with options to add, delete, update, view standings, simulate races, view race table, save data, load data, and exit the program.

## Technologies Used

- Python

## Author

- [Author](nisal2002) - Initial work

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
