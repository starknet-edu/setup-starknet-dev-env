import subprocess, json
from utils import str_to_felt, get_random_values

# essential settings
account_addr = "0x33507ff2edf12c12c73d0b6d1d90de9fac12a355de1097ab305249612451919"
salt = 1
contract_address = "0x"
pkey_name = ".pkey"
network = "devnet"
max_fee = "auto"

def run_command(cmd):
  out = subprocess.check_output(cmd.split(" "))
  return out.decode("utf-8")

# Build
def build():
  print("BUILD")
  run_command("protostar build")
  return

# Test
def test():
  print("TEST")
  run_command("protostar test")
  return

# Declare
def declare_and_deploy():
  print("DECLARE AND DEPLOY")
  out = run_command(f"protostar -p {network} declare ./build/main.json --account-address {account_addr} --private-key-path ./{pkey_name} --max-fee {max_fee} --wait-for-acceptance --json")

  class_hash = json.loads(out)['class_hash']

  print("--- CLASS_HASH: ", class_hash)

  out = run_command(f"protostar -p {network} deploy {class_hash} --account-address {account_addr} --private-key-path ./{pkey_name} --max-fee {max_fee} --wait-for-acceptance --json")

  global contract_address
  contract_address = json.loads(out)['contract_address']

  print("--- CONTRACT_ADDRESS: ", contract_address)

  return

# CALL
def call():
  print("CALL")
  out = run_command(f"protostar -p {network} call --contract-address {contract_address} --function get_balance --json")
  print("--- Result: ", json.loads(out)['transformed_output']['res'])
  return

# INVOKE
def invoke():
  print("INVOKE")
  run_command(f"protostar -p {network} invoke --contract-address {contract_address} --function increase_balance --account-address {account_addr} --inputs 8 --max-fee {max_fee} --private-key-path ./{pkey_name} --wait-for-acceptance --json")

  return

def main():
  build()
  test()
  declare_and_deploy()
  call()
  invoke()
  call()

main()