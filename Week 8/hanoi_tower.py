'''
    Parameters:
        Recursive function with four parameters:
            Number of disks to be moved
            Peg on which these disks are initially threaded
            Peg to which this stack of disks is to be moved
            Peg to be used as temporary holding area
'''

def hanoiTower(n, from_peg, to_peg, temp_peg):
    if n == 0:
        return
    hanoiTower(n-1, from_peg, temp_peg, to_peg)
    print(f"{from_peg} --> {to_peg}")
    hanoiTower(n-1, temp_peg, to_peg, from_peg)


def main():
    n_disks = int(input("Enter the number of disks between 1 and 10: "))
    print("Moving thse disk from peg 1 to peg 3")
    hanoiTower(n_disks, 1, 3, 2)

min()