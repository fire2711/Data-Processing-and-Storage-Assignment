This project is a small in-memory key-value store that supports a single transaction at a time. Any write done inside a transaction stays hidden until the transaction is committed. Rolling back a transaction discards all uncommitted changes.

---

## How to Run

1. Ensure that Python is installed.
2. Run the demo script:

   ```bash
   py main.py


How This Assignment Could Be Improved
This assignment could be modified in order to become an "official" assignment in the future by making the directions a little more clear. It may help to clearly define how get() should behave during transactions. Another improvement woud be adding a few required unit tests so that grading is more consistent and is easier to autmate. Furthermore, having an example output format would also be helpful.
