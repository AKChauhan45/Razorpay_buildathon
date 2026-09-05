import csv
with open('data/bank.csv') as f:
    r = csv.DictReader(f)
    for row in r:
        if row['txn_id'] in ('B002', 'B004', 'B009', 'B010'):
            print(f"Bank {row['txn_id']}: {row['description']} ({row['amount']})")

print('---')

with open('data/ledger.csv') as f:
    r = csv.DictReader(f)
    for row in r:
        if row.get('id') in ('L002', 'L004', 'L009', 'L010') or row.get('txn_id') in ('L002', 'L004', 'L009', 'L010'):
            print(f"Ledger {row.get('txn_id') or row.get('id')}: {row['description']} ({row['amount']})")
