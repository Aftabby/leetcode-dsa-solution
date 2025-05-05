"""
problem_name = Second Highest Salary
problem_source = https://leetcode.com/problems/second-highest-salary/description/

Algo
    -
"""

import pandas as pd


def main():
    test()


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    try:
        return pd.DataFrame(
            [employee["salary"].drop_duplicates().nlargest(2).iloc[1]],
            columns=["SecondHighestSalary"],
        )
    except IndexError:
        return pd.DataFrame([[None]], columns=["SecondHighestSalary"])


def test():
    # Schema
    # Test1
    data = [[1, 100], [2, 200], [3, 300]]
    employee = pd.DataFrame(data, columns=["id", "salary"]).astype(
        {"id": "int64", "salary": "int64"}
    )
    print(second_highest_salary(employee))

    # Test2
    data = [[1, 100]]
    employee = pd.DataFrame(data, columns=["id", "salary"]).astype(
        {"id": "int64", "salary": "int64"}
    )
    print(second_highest_salary(employee))

    # Test3
    data = [[1, 100], [2, 300], [3, 300]]
    employee = pd.DataFrame(data, columns=["id", "salary"]).astype(
        {"id": "int64", "salary": "int64"}
    )
    print(second_highest_salary(employee))


if __name__ == "__main__":
    main()
