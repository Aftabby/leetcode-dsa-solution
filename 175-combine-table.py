import pandas as pd


"""
problem_name = Combine Two Tables
problem_source = https://leetcode.com/problems/combine-two-tables/description/

Algo
    -
"""


def main():
    test()


def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    full_df = person.merge(address, on="personId", how="left")
    return full_df[["firstName", "lastName", "city", "state"]]


def test():
    # Schema
    data = [[1, "Wang", "Allen"], [2, "Alice", "Bob"]]
    person = pd.DataFrame(data, columns=["personId", "firstName", "lastName"]).astype(
        {"personId": "Int64", "firstName": "object", "lastName": "object"}
    )

    data = [[1, 2, "New York City", "New York"], [2, 3, "Leetcode", "California"]]
    address = pd.DataFrame(
        data, columns=["addressId", "personId", "city", "state"]
    ).astype(
        {"addressId": "Int64", "personId": "Int64", "city": "object", "state": "object"}
    )

    print(combine_two_tables(person, address))


if __name__ == "__main__":
    main()
