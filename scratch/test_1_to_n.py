import csv
from datetime import datetime
import itertools
from backend.reconciler import Reconciler

r = Reconciler()
r.consumed_bank_ids = set()
r.consumed_ledger_ids = set()

bank_data = []
with open('data/bank.csv') as f:
    bank_data = list(csv.DictReader(f))

ledger_data = []
with open('data/ledger.csv') as f:
    ledger_data = list(csv.DictReader(f))

b004 = next(b for b in bank_data if b['txn_id'] == 'B004')
l004a = next(l for l in ledger_data if l.get('txn_id', l.get('id')) == 'L004A')
l004b = next(l for l in ledger_data if l.get('txn_id', l.get('id')) == 'L004B')

print("B004:", b004)
print("L004A:", l004a)
print("L004B:", l004b)

res = r._find_1_to_N(b004, [l004a, l004b])
print("Match result:", res)
