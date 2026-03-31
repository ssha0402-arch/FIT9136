"""
Database management (question 1)
"""
# import all necessary module(s)&function(s)
import copy


def create_new_copy(table: list) -> list:
    """
    Creates a deep copy of the input list and returns it.
    @param table the input table to copy
    @return a copy of the table
    """
    return copy.deepcopy(table)

def add_row(row: list, table: list) -> None:
    """
    Adds the given row at the bottom of the table.
    @param row the row to add.
    @param table the table to add the row to.
    """
    table.append(row)

def delete_row(index, table) -> None:
    """
    Deletes the row at the given index from the given table.
    @param index the index of the row to delete.
    @param table the table to delete the row from.
    """
    del table[index]

def insert_row(index: int, row: list, table: list) -> None:
    """
    Inserts a row in the table at a given index.
    @param index the index where to insert.
    @param row the row to insert.
    @param table the table in which to insert the tow.
    """
    table.insert(index, row)

def edit_row(index: int, row: list, table: list) -> None:
    """
    Replaces a row of the table at a given index by another row.
    @param index the index of the row to edit.
    @param row the row to use.
    @param table the table in which to edit the tow.
    """
    table[index] = row

def add_column(column, table) -> None:
    """
    Adds the column to the table, or if the sizes do no match,
    prints an error message.
    @param column the column to insert.
    @param table the table in which to insert the column.
    """
    # Check if the length of the column matches the number of rows in the table
    if len(column) == len(table):
        # Iterate over each row and append the corresponding column value
        for i in range(len(table)):
            table[i].append(column[i])
    # Print error if sizes do not match
    else:
        print("Error: The number of rows in the input table do not match with the number of rows in the new input column.")

if __name__ == "__main__":

    small_table = [['A', 'B'], ['C', 'D'], ['E', 'F']]
    new_small_table = create_new_copy(small_table)
    print(new_small_table)
    [['A', 'B'], ['C', 'D'], ['E', 'F']]

    add_row(['G', 'H'], new_small_table)
    print(new_small_table)
    [['A', 'B'], ['C', 'D'], ['E', 'F'], ['G', 'H']]

    delete_row(1, new_small_table)
    print(new_small_table)
    [['A', 'B'], ['E', 'F'], ['G', 'H']]

    insert_row(1, ['c', 'd'], new_small_table)
    print(new_small_table)
    [['A', 'B'], ['c', 'd'], ['E', 'F'], ['G', 'H']]

    edit_row(2, ['e', 'f'], new_small_table)
    print(new_small_table)
    [['A', 'B'], ['c', 'd'], ['e', 'f'], ['G', 'H']]

    add_column(['*', '!'], new_small_table)
    # Error: The number of rows in the input table do not match with the number of rows in the new input column.
    
    add_column(['*', '!', '?', '.'], new_small_table)
    print(new_small_table)
    [['A', 'B', '*'], ['c', 'd', '!'], ['e', 'f', '?'], ['G', 'H', '.']]
