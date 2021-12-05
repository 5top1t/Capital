# Capital
Wealth consists not in having great possessions, but in having few wants. --Epictetus

Credit card transactions are hard to grok at a glance due to noise. Payments blend in with transactions, transactions to the same store in multiple locations are hard to identify, and sometimes you want omit transaction you expect to be present. Capital is a data cleansing tool that accepts raw transactions exports from banks.

### __Banks__
Supported
- Apple Card - `apple`
- Bank of America - `boa`
- Capital One - `capone`
  
### __Key Features__

- Multiple bank are supported
- User friendly payee names
- Drop recurring transactions
- Filter transactions after a date
- Filter transactions within a month

# __Getting started__
Clone __Capital__ to a local directory called `path` and create an alias for it. 
```bash
alias capital="python3 {path}/Capital/runner.py"
```

### Arguments
| Option | Description |  Type  |  Options  | Required |
| ------ | ----------- | ------ | -------- | --- |
| -bank  | Bank to be processed | String | `capone`, `boa` | ✔️ |
| -file  | Transaction exports file path | CSV | | ✔️ |
| -month | Filter transactions for the given month | Number | `1-12` |  |
| -date | Filter transactions after a given date (inclusive) | Date | `mm/dd/yyy` |  |

### Example
Clean Bank of America transactions for November after the 9th.
```bash
capital -bank boa -file ~/Downloads/currentTransaction.csv -month 11 -date 11/9/2021
```



