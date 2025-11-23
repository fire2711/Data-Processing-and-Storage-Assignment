from in_memory_db import InMemoryDB, TransactionError


def demo_scenario_1() -> None:
    print("=== Scenario 1 ===")
    inmemoryDB = InMemoryDB()

    # should return None, because A doesn’t exist in the DB yet
    print("get('A') ->", inmemoryDB.get("A"))

    # should throw an error because a transaction is not in progress
    try:
        inmemoryDB.put("A", 5)
    except TransactionError as e:
        print("put('A', 5) raised:", e)

    # starts a new transaction
    inmemoryDB.begin_transaction()
    print("begin_transaction()")

    # set’s value of A to 5, but it's not committed yet
    inmemoryDB.put("A", 5)
    print("put('A', 5) inside transaction")

    # should return None, because updates to A are not committed yet
    print("get('A') during transaction ->", inmemoryDB.get("A"))

    # update A’s value to 6 within the transaction
    inmemoryDB.put("A", 6)
    print("put('A', 6) inside transaction")

    # commits the open transaction
    inmemoryDB.commit()
    print("commit()")

    # should return 6, that was the last value of A to be committed
    print("get('A') after commit ->", inmemoryDB.get("A"))

    # throws an error, because there is no open transaction
    try:
        inmemoryDB.commit()
    except TransactionError as e:
        print("commit() with no transaction raised:", e)

    # throws an error because there is no ongoing transaction
    try:
        inmemoryDB.rollback()
    except TransactionError as e:
        print("rollback() with no transaction raised:", e)


def demo_scenario_2() -> None:
    print("\n=== Scenario 2 ===")
    inmemoryDB = InMemoryDB()

    # should return None because B does not exist in the database
    print("get('B') ->", inmemoryDB.get("B"))

    # starts a new transaction
    inmemoryDB.begin_transaction()
    print("begin_transaction()")

    # Set key B’s value to 10 within the transaction
    inmemoryDB.put("B", 10)
    print("put('B', 10) inside transaction")

    # Rollback the transaction - revert any changes made to B
    inmemoryDB.rollback()
    print("rollback()")

    # Should return None because changes to B were rolled back
    print("get('B') after rollback ->", inmemoryDB.get("B"))


if __name__ == "__main__":
    demo_scenario_1()
    demo_scenario_2()
