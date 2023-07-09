""" leetcode: 1672. Richest Customer Wealth"""

def maximumWealth(accounts) -> int:
    """ You are given an m x n integer grid accounts where accounts[i][j]
    is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the
    wealth that the richest customer has."""
    max = 0
    for cust in accounts:
        wealth = sum(accounts[accounts.index(cust)])
        if wealth > max:
            max = wealth
    return max


accounts = [[1,2,3],[3,2,1]]
print (maximumWealth(accounts))
accounts = [[1,5],[7,3],[3,5]]
print (maximumWealth(accounts))
accounts = [[2,8,7],[7,1,3],[1,9,5]]
print (maximumWealth(accounts))
