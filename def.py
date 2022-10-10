# Palkeoramix decompiler. 

const unknown20606b70 = 0x8b73c3c69bb8fe3d512ecc4cf759cc79239f7b179b0ffacaa9a75d522b39400f
const decimals = 18
const unknown9e4e7318 = 0xc89efdaa54c0f20c7adf612882df0950f5a951637e0307cdcb4c672f298b8bc6
const PERMIT_TYPEHASH = 0x6e71edae12b1b97f4d1f60370fef10105fa2faae0126114a169c64845d6126c9

def storage:
  name is array of struct at storage 0
  symbol is array of uint256 at storage 1
  totalSupply is uint256 at storage 2
  allowance is mapping of uint256 at storage 3
  balanceOf is mapping of uint256 at storage 4
  nonces is mapping of uint256 at storage 5
  owner is addr at storage 6
  unknown3bdc6e72 is uint256 at storage 7
  stor8 is mapping of uint8 at storage 8
  totalDeposits is uint256 at storage 9
  unknownc89039c5Address is addr at storage 10
  rewardTokenAddress is addr at storage 11
  devAddr is addr at storage 12
  unknownbd079f55 is uint256 at storage 13
  unknown789139bc is uint256 at storage 14
  unknownb52a321f is uint8 at storage 15
  unknown8aff733d is uint256 at storage 16
  unknown07677111 is uint256 at storage 17
  unknown5ea682ea is uint256 at storage 18
  stakingContractAddress is addr at storage 19
  unknownf887ea40Address is addr at storage 20

def name() payable: 
  return name[0 len name.length].field_0

def unknown07677111() payable: 
  return unknown07677111

def totalSupply() payable: 
  return totalSupply

def unknown3bdc6e72() payable: 
  return unknown3bdc6e72

def unknown483c2ef0(addr _param1) payable: 
  require calldata.size - 4 >= 32
  return bool(stor8[_param1])

def unknown5ea682ea() payable: 
  return unknown5ea682ea

def balanceOf(address _owner) payable: 
  require calldata.size - 4 >= 32
  return balanceOf[addr(_owner)]

def unknown789139bc() payable: 
  return unknown789139bc

def totalDeposits() payable: 
  return totalDeposits

def nonces(address _param1) payable: 
  require calldata.size - 4 >= 32
  return nonces[_param1]

def unknown8aff733d() payable: 
  return unknown8aff733d

def owner() payable: 
  return owner

def symbol() payable: 
  return symbol[0 len symbol.length]

def unknownb52a321f() payable: 
  return bool(unknownb52a321f)

def unknownbd079f55() payable: 
  return unknownbd079f55

def unknownc89039c5() payable: 
  return unknownc89039c5Address

def devAddr() payable: 
  return devAddr

def allowance(address _owner, address _spender) payable: 
  require calldata.size - 4 >= 64
  return allowance[addr(_owner)][addr(_spender)]

def stakingContract() payable: 
  return stakingContractAddress

def rewardToken() payable: 
  return rewardTokenAddress

def unknownf887ea40() payable: 
  return unknownf887ea40Address

#
#  Regular functions
#

def _fallback() payable: # default function
  revert

def unknown9291d563(addr _param1) payable: 
  require calldata.size - 4 >= 32
  require caller == devAddr
  log 0xa8e91499: devAddr, _param1
  devAddr = _param1

def renounceOwnership() payable: 
  if owner != caller:
      revert with 0, 'wOwnable: caller is not the owne'
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=0)
  owner = 0

def unknown81837230(uint256 _param1) payable: 
  require calldata.size - 4 >= 32
  if owner != caller:
      revert with 0, 'wOwnable: caller is not the owne'
  log 0x481f79ac: unknownbd079f55, _param1
  unknownbd079f55 = _param1

def unknowne21ac825(uint256 _param1) payable: 
  require calldata.size - 4 >= 32
  if owner != caller:
      revert with 0, 'wOwnable: caller is not the owne'
  log 0xa5dae505: unknown789139bc, _param1
  unknown789139bc = _param1

def unknown4e77ace5(bool _param1) payable: 
  require calldata.size - 4 >= 32
  if owner != caller:
      revert with 0, 'wOwnable: caller is not the owne'
  require _param1 != bool(unknownb52a321f)
  unknownb52a321f = uint8(_param1)
  log 0x7b014ed3: _param1

def checkReward() payable: 
  require ext_code.size(stakingContractAddress)
  static call stakingContractAddress.0x8cc262 with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]

def unknown0f23475d() payable: 
  require ext_code.size(stakingContractAddress)
  static call stakingContractAddress.balanceOf(address tokenOwner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]

def unknown4ebb7916(uint256 _param1) payable: 
  require calldata.size - 4 >= 32
  if owner != caller:
      revert with 0, 'wOwnable: caller is not the owne'
  require _param1 > 0
  call caller with:
     value _param1 wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  log Recovered(
        address recoveredTo=0,
        uint256 amount=_param1)

def approve(address _spender, uint256 _value) payable: 
  require calldata.size - 4 >= 64
  if not caller:
      revert with 0, '_approve::owner zero address'
  if not _spender:
      revert with 0, '_approve::spender zero address'
  allowance[caller][addr(_spender)] = _value
  log Approval(
        address tokenOwner=_value,
        address spender=caller,
        uint256 tokens=_spender)
  return 1

def unknown4bebd1e7(addr _param1) payable: 
  require calldata.size - 4 >= 32
  if owner != caller:
      revert with 0, 'wOwnable: caller is not the owne'
  if stor8[addr(_param1)]:
      revert with 0, 'Permissioned::allowDepositor'
  stor8[addr(_param1)] = 1
  if unknown3bdc6e72 + 1 < unknown3bdc6e72:
      revert with 0, 'SafeMath: addition overflow'
  unknown3bdc6e72++
  log 0xc0a1035c: _param1

def updateAdminFee(uint256 _param1) payable: 
  require calldata.size - 4 >= 32
  if owner != caller:
      revert with 0, 'wOwnable: caller is not the owne'
  if unknown5ea682ea + _param1 < _param1:
      revert with 0, 'SafeMath: addition overflow'
  if unknown8aff733d < 0:
      revert with 0, 'SafeMath: addition overflow'
  require unknown8aff733d + unknown5ea682ea + _param1 <= 10000
  log 0x3cc372f3: unknown07677111, _param1
  unknown07677111 = _param1

def unknown99729ec1(uint256 _param1) payable: 
  require calldata.size - 4 >= 32
  if owner != caller:
      revert with 0, 'wOwnable: caller is not the owne'
  if unknown07677111 + _param1 < _param1:
      revert with 0, 'SafeMath: addition overflow'
  if unknown8aff733d < 0:
      revert with 0, 'SafeMath: addition overflow'
  require unknown8aff733d + unknown07677111 + _param1 <= 10000
  log 0x2a42303d: unknown5ea682ea, _param1
  unknown5ea682ea = _param1

def unknowna8ae2b7c(uint256 _param1) payable: 
  require calldata.size - 4 >= 32
  if owner != caller:
      revert with 0, 'wOwnable: caller is not the owne'
  if unknown07677111 + _param1 < _param1:
      revert with 0, 'SafeMath: addition overflow'
  if unknown5ea682ea < 0:
      revert with 0, 'SafeMath: addition overflow'
  require unknown5ea682ea + unknown07677111 + _param1 <= 10000
  log 0xe7f97d51: unknown8aff733d, _param1
  unknown8aff733d = _param1

def revokeAllowance(address _param1, address _param2) payable: 
  require calldata.size - 4 >= 64
  if owner != caller:
      revert with 0, 'wOwnable: caller is not the owne'
  require ext_code.size(_param1)
  call _param1.approve(address spender, uint256 tokens) with:
       gas gas_remaining wei
      args addr(_param2), 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]

def transferOwnership(address _newOwner) payable: 
  require calldata.size - 4 >= 32
  if owner != caller:
      revert with 0, 'wOwnable: caller is not the owne'
  if not _newOwner:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  38,
                  0x734f776e61626c653a206e6577206f776e657220697320746865207a65726f20616464726573,
                  mem[202 len 26]
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  owner = _newOwner

def unknowned24911d() payable: 
  mem[96] = uint256(name.field_0)
  idx = 96
  s = 0
  while name.length + 96 > idx + 32:
      mem[idx + 32] = name[s].field_256
      idx = idx + 32
      s = s + 1
      continue 
  return sha3(0x8b73c3c69bb8fe3d512ecc4cf759cc79239f7b179b0ffacaa9a75d522b39400f, sha3(mem[96 len name.length]), 0xc89efdaa54c0f20c7adf612882df0950f5a951637e0307cdcb4c672f298b8bc6, chainid, this.address)

def recoverERC20(address _tokenAddress, uint256 _tokens) payable: 
  require calldata.size - 4 >= 64
  if owner != caller:
      revert with 0, 'wOwnable: caller is not the owne'
  require _tokens > 0
  require ext_code.size(_tokenAddress)
  call _tokenAddress.transfer(address to, uint256 tokens) with:
       gas gas_remaining wei
      args caller, _tokens
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  log Recovered(
        address recoveredTo=addr(_tokenAddress),
        uint256 amount=_tokens)

def unknownb9e57b80() payable: 
  require ext_code.size(stakingContractAddress)
  static call stakingContractAddress.0x8cc262 with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data < unknownbd079f55:
      return 0
  if not ext_call.return_data[0]:
      return 0
  if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  33,
                  0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                  mem[197 len 31]
  return (unknown8aff733d * ext_call.return_data / 10000)

def unknown8b73e606(addr _param1) payable: 
  require calldata.size - 4 >= 32
  if owner != caller:
      revert with 0, 'wOwnable: caller is not the owne'
  if unknown3bdc6e72 <= 0:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  52,
                  0x645065726d697373696f6e65643a3a72656d6f76654465706f7369746f722c206e6f20616c6c6f776564206465706f7369746f72,
                  mem[216 len 12]
  if bool(stor8[addr(_param1)]) != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  42,
                  0x735065726d697373696f6e65643a3a72656d6f76654465706f7369746f722c206e6f7420616c6c6f7765,
                  mem[206 len 22]
  stor8[addr(_param1)] = 0
  if 1 > unknown3bdc6e72:
      revert with 0, 'SafeMath: subtraction underflow'
  unknown3bdc6e72--
  log 0xe86f6608: _param1

def unknowneab89a5a(uint256 _param1) payable: 
  require calldata.size - 4 >= 32
  if not totalSupply:
      return 0
  if totalDeposits * totalSupply / totalSupply != totalDeposits:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  33,
                  0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                  mem[197 len 31]
  if not totalDeposits * totalSupply:
      return 0
  if not _param1:
      if not totalSupply:
          revert with 0, 'SafeMath: division by zero'
      return (0 / totalSupply)
  if totalDeposits * _param1 / _param1 != totalDeposits:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  33,
                  0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                  mem[197 len 31]
  if not totalSupply:
      revert with 0, 'SafeMath: division by zero'
  return (totalDeposits * _param1 / totalSupply)

def unknowndd8ce4d6(uint256 _param1) payable: 
  require calldata.size - 4 >= 32
  if not totalSupply:
      return _param1
  if totalDeposits * totalSupply / totalSupply != totalDeposits:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  33,
                  0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                  mem[197 len 31]
  if not totalDeposits * totalSupply:
      return _param1
  if not _param1:
      if not totalDeposits:
          revert with 0, 'SafeMath: division by zero'
      return (0 / totalDeposits)
  if totalSupply * _param1 / _param1 != totalSupply:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  33,
                  0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                  mem[197 len 31]
  if not totalDeposits:
      revert with 0, 'SafeMath: division by zero'
  return (totalSupply * _param1 / totalDeposits)

def transfer(address _to, uint256 _value) payable: 
  require calldata.size - 4 >= 64
  if not _to:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  52,
                  0x725f7472616e73666572546f6b656e733a2063616e6e6f74207472616e7366657220746f20746865207a65726f20616464726573,
                  mem[216 len 12]
  if _value > balanceOf[caller]:
      revert with 0, 
                  32,
                  46,
                  0x655f7472616e73666572546f6b656e733a207472616e7366657220657863656564732066726f6d2062616c616e63,
                  mem[174 len 18],
                  mem[210 len 14]
  balanceOf[caller] -= _value
  if _value + balanceOf[_to] < balanceOf[_to]:
      revert with 0, 'SafeMath: addition overflow'
  balanceOf[addr(_to)] = _value + balanceOf[_to]
  log Transfer(
        address from=_value,
        address to=caller,
        uint256 tokens=_to)
  return 1

def unknownac0d31ff(uint256 _param1, bool _param2) payable: 
  require calldata.size - 4 >= 64
  if owner != caller:
      revert with 0, 'wOwnable: caller is not the owne'
  require ext_code.size(unknownc89039c5Address)
  static call unknownc89039c5Address.balanceOf(address tokenOwner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(stakingContractAddress)
  call stakingContractAddress.exit() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(unknownc89039c5Address)
  static call unknownc89039c5Address.balanceOf(address tokenOwner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data > ext_call.return_data[0]:
      revert with 0, 'SafeMath: subtraction underflow'
  if 0 < _param1:
      revert with 0, 32, 34, 0xfe446578537472617465677956343a3a7265736375654465706c6f79656446756e64, mem[262 len 30]
  totalDeposits = ext_call.return_data[0]
  log 0xc7606d21: ext_call.return_data
  if 1 == bool(unknownb52a321f):
      if _param2 == 1:
          if owner != caller:
              revert with 0, 'wOwnable: caller is not the owne'
          require unknownb52a321f
          unknownb52a321f = 0
          log 0x7b014ed3: 0

def setAllowances() payable: 
  if owner != caller:
      revert with 0, 'wOwnable: caller is not the owne'
  require ext_code.size(unknownc89039c5Address)
  call unknownc89039c5Address.approve(address spender, uint256 tokens) with:
       gas gas_remaining wei
      args stakingContractAddress, -1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(rewardTokenAddress)
  call rewardTokenAddress.approve(address spender, uint256 tokens) with:
       gas gas_remaining wei
      args unknownf887ea40Address, -1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(unknownc89039c5Address)
  static call unknownc89039c5Address.0xdfe1681 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data))
  call addr(ext_call.return_data).approve(address spender, uint256 tokens) with:
       gas gas_remaining wei
      args unknownf887ea40Address, -1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(unknownc89039c5Address)
  static call unknownc89039c5Address.token1() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data))
  call addr(ext_call.return_data).approve(address spender, uint256 tokens) with:
       gas gas_remaining wei
      args unknownf887ea40Address, -1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32

def unknownd505accf(addr _param1, addr _param2, uint256 _param3, uint256 _param4, uint8 _param5, uint256 _param6, uint256 _param7) payable: 
  require calldata.size - 4 >= 224
  if _param4 < block.timestamp:
      revert with 0, 'permit::expired'
  nonces[addr(_param1)]++
  mem[320] = uint256(name.field_0)
  idx = 320
  s = 0
  while name.length + 320 > idx + 32:
      mem[idx + 32] = name[s].field_256
      idx = idx + 32
      s = s + 1
      continue 
  signer = erecover(sha3(0, sha3(0x8b73c3c69bb8fe3d512ecc4cf759cc79239f7b179b0ffacaa9a75d522b39400f, sha3(mem[320 len name.length]), 0xc89efdaa54c0f20c7adf612882df0950f5a951637e0307cdcb4c672f298b8bc6, chainid, this.address), sha3(0x6e71edae12b1b97f4d1f60370fef10105fa2faae0126114a169c64845d6126c9, addr(_param1), addr(_param2), _param3, nonces[addr(_param1)], _param4)), _param5 << 248, _param6, _param7) # precompiled
  if not erecover.result:
      revert with ext_call.return_data[0 len return_data.size]
  if not addr(signer):
      revert with 0, 
                  32,
                  36,
                  0x73417263683a3a76616c69646174655369673a20696e76616c6964207369676e61747572,
                  Mask(192, 0, _param7),
                  mem[770 len 4]
  if addr(signer) != _param1:
      revert with 0, 
                  32,
                  36,
                  0x73417263683a3a76616c69646174655369673a20696e76616c6964207369676e61747572,
                  Mask(192, 0, _param7),
                  mem[770 len 4]
  if not _param1:
      revert with 0, '_approve::owner zero address'
  if not _param2:
      revert with 0, '_approve::spender zero address'
  allowance[addr(_param1)][addr(_param2)] = _param3
  log Approval(
        address tokenOwner=_param3,
        address spender=_param1,
        uint256 tokens=_param2)

def transferFrom(address _from, address _to, uint256 _value) payable: 
  require calldata.size - 4 >= 96
  if caller == _from:
      if not _to:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      32,
                      52,
                      0x725f7472616e73666572546f6b656e733a2063616e6e6f74207472616e7366657220746f20746865207a65726f20616464726573,
                      mem[216 len 12]
      if _value > balanceOf[addr(_from)]:
          revert with 0, 
                      32,
                      46,
                      0x655f7472616e73666572546f6b656e733a207472616e7366657220657863656564732066726f6d2062616c616e63,
                      mem[174 len 18],
                      mem[210 len 14]
  else:
      if allowance[addr(_from)][caller] == -1:
          if not _to:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          52,
                          0x725f7472616e73666572546f6b656e733a2063616e6e6f74207472616e7366657220746f20746865207a65726f20616464726573,
                          mem[216 len 12]
          if _value > balanceOf[addr(_from)]:
              revert with 0, 
                          32,
                          46,
                          0x655f7472616e73666572546f6b656e733a207472616e7366657220657863656564732066726f6d2062616c616e63,
                          mem[174 len 18],
                          mem[210 len 14]
      else:
          if _value > allowance[addr(_from)][caller]:
              revert with 0, 
                          32,
                          47,
                          0x737472616e7366657246726f6d3a207472616e7366657220616d6f756e74206578636565647320616c6c6f77616e63,
                          mem[175 len 17],
                          mem[209 len 15]
          allowance[addr(_from)][caller] = allowance[addr(_from)][caller] - _value
          log Approval(
                address tokenOwner=(allowance[addr(_from)][caller] - _value),
                address spender=_from,
                uint256 tokens=caller)
          if not _to:
              revert with 0, 
                          32,
                          52,
                          0x725f7472616e73666572546f6b656e733a2063616e6e6f74207472616e7366657220746f20746865207a65726f20616464726573,
                          mem[312 len 12]
          if _value > balanceOf[addr(_from)]:
              revert with 0, 
                          32,
                          46,
                          0x655f7472616e73666572546f6b656e733a207472616e7366657220657863656564732066726f6d2062616c616e63,
                          mem[270 len 18],
                          mem[306 len 14]
  ('le', ('param', '_value'), ('stor', ('map', ('mask_shl', 160, 0, 0, ('param', '_from')), ('name', 'balanceOf', 4))))
  balanceOf[addr(_from)] -= _value
  if _value + balanceOf[_to] < balanceOf[_to]:
      revert with 0, 'SafeMath: addition overflow'
  balanceOf[addr(_to)] = _value + balanceOf[_to]
  log Transfer(
        address from=_value,
        address to=_from,
        uint256 tokens=_to)
  return 1

def withdraw(uint256 _amount) payable: 
  require calldata.size - 4 >= 32
  if totalSupply:
      if totalDeposits * totalSupply / totalSupply != totalDeposits:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      32,
                      33,
                      0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                      mem[197 len 31]
      if totalDeposits * totalSupply:
          if not _amount:
              if not totalSupply:
                  revert with 0, 'SafeMath: division by zero'
              if 0 / totalSupply:
                  if 0 / totalSupply <= 0:
                      revert with 0, 32, 37, 0x65446578537472617465677956343a3a5f77697468647261774465706f736974546f6b656e, mem[265 len 27]
                  require ext_code.size(stakingContractAddress)
                  call stakingContractAddress.withdraw(uint256 withdrawCount) with:
                       gas gas_remaining wei
                      args (0 / totalSupply)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(unknownc89039c5Address)
                  call unknownc89039c5Address.transfer(address to, uint256 tokens) with:
                       gas gas_remaining wei
                      args caller, 0 / totalSupply
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if not ext_call.return_data[0]:
                      revert with 0, 'DexStrategyV4::withdraw'
                  if _amount > balanceOf[caller]:
                      revert with 0, 
                                  32,
                                  39,
                                  0x655f6275726e3a206275726e20616d6f756e7420657863656564732066726f6d2062616c616e63,
                                  mem[231 len 25],
                                  mem[281 len 7]
                  balanceOf[caller] -= _amount
                  if _amount > totalSupply:
                      revert with 0, 
                                  32,
                                  39,
                                  0x735f6275726e3a206275726e20616d6f756e74206578636565647320746f74616c20737570706c,
                                  mem[327 len 25],
                                  mem[377 len 7]
                  totalSupply -= _amount
                  log Transfer(
                        address from=_amount,
                        address to=caller,
                        uint256 tokens=0)
                  if 0 / totalSupply > totalDeposits:
                      revert with 0, 'SafeMath: subtraction underflow'
                  totalDeposits -= 0 / totalSupply
                  log Withdraw(
                        address owner=(0 / totalSupply),
                        uint256 value=caller)
          else:
              if totalDeposits * _amount / _amount != totalDeposits:
                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                              32,
                              33,
                              0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                              mem[197 len 31]
              if not totalSupply:
                  revert with 0, 'SafeMath: division by zero'
              if totalDeposits * _amount / totalSupply:
                  if totalDeposits * _amount / totalSupply <= 0:
                      revert with 0, 32, 37, 0x65446578537472617465677956343a3a5f77697468647261774465706f736974546f6b656e, mem[265 len 27]
                  require ext_code.size(stakingContractAddress)
                  call stakingContractAddress.withdraw(uint256 withdrawCount) with:
                       gas gas_remaining wei
                      args (totalDeposits * _amount / totalSupply)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(unknownc89039c5Address)
                  call unknownc89039c5Address.transfer(address to, uint256 tokens) with:
                       gas gas_remaining wei
                      args caller, totalDeposits * _amount / totalSupply
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if not ext_call.return_data[0]:
                      revert with 0, 'DexStrategyV4::withdraw'
                  if _amount > balanceOf[caller]:
                      revert with 0, 
                                  32,
                                  39,
                                  0x655f6275726e3a206275726e20616d6f756e7420657863656564732066726f6d2062616c616e63,
                                  mem[231 len 25],
                                  mem[281 len 7]
                  balanceOf[caller] -= _amount
                  if _amount > totalSupply:
                      revert with 0, 
                                  32,
                                  39,
                                  0x735f6275726e3a206275726e20616d6f756e74206578636565647320746f74616c20737570706c,
                                  mem[327 len 25],
                                  mem[377 len 7]
                  totalSupply -= _amount
                  log Transfer(
                        address from=_amount,
                        address to=caller,
                        uint256 tokens=0)
                  if totalDeposits * _amount / totalSupply > totalDeposits:
                      revert with 0, 'SafeMath: subtraction underflow'
                  totalDeposits -= totalDeposits * _amount / totalSupply
                  log Withdraw(
                        address owner=(totalDeposits * _amount / totalSupply),
                        uint256 value=caller)

def reinvest() payable: 
  if tx.origin != caller:
      revert with 0, 'YakStrategy::onlyEOA'
  require ext_code.size(stakingContractAddress)
  static call stakingContractAddress.0x8cc262 with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data < unknownbd079f55:
      revert with 0, 'DexStrategyV4::reinvest'
  require ext_code.size(stakingContractAddress)
  call stakingContractAddress.getReward() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  if not ext_call.return_data[0]:
      if not ext_call.return_data[0]:
          if not ext_call.return_data[0]:
              if 0 > ext_call.return_data[0]:
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              if ext_call.return_data / 2 <= 0:
                  revert with 0, 
                              32,
                              50,
                              0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                              mem[662 len 14]
              require ext_code.size(unknownc89039c5Address)
              static call unknownc89039c5Address.0xdfe1681 with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[608] = ext_call.return_data[12 len 20]
              if rewardTokenAddress != mem[620 len 20]:
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              require ext_code.size(unknownc89039c5Address)
              static call unknownc89039c5Address.token1() with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[704] = ext_call.return_data[12 len 20]
              if rewardTokenAddress != mem[716 len 20]:
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              require ext_code.size(unknownf887ea40Address)
              call unknownf887ea40Address.0xe8e33700 with:
                   gas gas_remaining wei
                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataaddr(this.address), block.timestamp
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 96
              if ext_call.return_data <= 0:
                  revert with 0, 
                              32,
                              34,
                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                              Mask(239, 1, ext_call.return_data[0])
          else:
              if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                  revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
              if unknown8aff733d * ext_call.return_data / 10000:
                  require ext_code.size(rewardTokenAddress)
                  call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                       gas gas_remaining wei
                      args caller, unknown8aff733d * ext_call.return_data / 10000
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if not ext_call.return_data[0]:
                      revert with 0, 'DexStrategyV4::_reinvest, reward'
              if 0 > ext_call.return_data[0]:
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              if unknown8aff733d * ext_call.return_data / 10000 > ext_call.return_data[0]:
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              if ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                  revert with 0, 
                              32,
                              50,
                              0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                              mem[662 len 14]
              require ext_code.size(unknownc89039c5Address)
              static call unknownc89039c5Address.0xdfe1681 with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[608] = ext_call.return_data[12 len 20]
              if rewardTokenAddress != mem[620 len 20]:
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              require ext_code.size(unknownc89039c5Address)
              static call unknownc89039c5Address.token1() with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[704] = ext_call.return_data[12 len 20]
              if rewardTokenAddress != mem[716 len 20]:
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              require ext_code.size(unknownf887ea40Address)
              call unknownf887ea40Address.0xe8e33700 with:
                   gas gas_remaining wei
                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 96
              if ext_call.return_data <= 0:
                  revert with 0, 
                              32,
                              34,
                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                              Mask(239, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000))
      else:
          if unknown07677111 * ext_call.return_data / ext_call.return_dataunknown07677111:
              revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[261 len 31]
          if unknown07677111 * ext_call.return_data / 10000:
              require ext_code.size(rewardTokenAddress)
              call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                   gas gas_remaining wei
                  args owner, unknown07677111 * ext_call.return_data / 10000
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'DexStrategyV4::_reinvest, admin'
          if not ext_call.return_data[0]:
              if 0 > ext_call.return_data[0]:
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              if unknown07677111 * ext_call.return_data / 10000 > ext_call.return_data[0]:
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              if 0 > ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                  revert with 0, 
                              32,
                              50,
                              0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                              mem[662 len 14]
              require ext_code.size(unknownc89039c5Address)
              static call unknownc89039c5Address.0xdfe1681 with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[608] = ext_call.return_data[12 len 20]
              if rewardTokenAddress != mem[620 len 20]:
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              require ext_code.size(unknownc89039c5Address)
              static call unknownc89039c5Address.token1() with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[704] = ext_call.return_data[12 len 20]
              if rewardTokenAddress != mem[716 len 20]:
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              require ext_code.size(unknownf887ea40Address)
              call unknownf887ea40Address.0xe8e33700 with:
                   gas gas_remaining wei
                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 96
              if ext_call.return_data <= 0:
                  revert with 0, 
                              32,
                              34,
                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                              Mask(239, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000))
          else:
              if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                  revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
              if unknown8aff733d * ext_call.return_data / 10000:
                  require ext_code.size(rewardTokenAddress)
                  call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                       gas gas_remaining wei
                      args caller, unknown8aff733d * ext_call.return_data / 10000
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if not ext_call.return_data[0]:
                      revert with 0, 'DexStrategyV4::_reinvest, reward'
              if 0 > ext_call.return_data[0]:
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              if unknown07677111 * ext_call.return_data / 10000 > ext_call.return_data[0]:
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              if unknown8aff733d * ext_call.return_data / 10000 > ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                  revert with 0, 
                              32,
                              50,
                              0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                              mem[662 len 14]
              require ext_code.size(unknownc89039c5Address)
              static call unknownc89039c5Address.0xdfe1681 with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[608] = ext_call.return_data[12 len 20]
              if rewardTokenAddress != mem[620 len 20]:
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              require ext_code.size(unknownc89039c5Address)
              static call unknownc89039c5Address.token1() with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[704] = ext_call.return_data[12 len 20]
              if rewardTokenAddress != mem[716 len 20]:
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              require ext_code.size(unknownf887ea40Address)
              call unknownf887ea40Address.0xe8e33700 with:
                   gas gas_remaining wei
                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 96
              if ext_call.return_data <= 0:
                  revert with 0, 
                              32,
                              34,
                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                              Mask(239, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
  else:
      if unknown5ea682ea * ext_call.return_data / ext_call.return_dataunknown5ea682ea:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      32,
                      33,
                      0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                      mem[197 len 31]
      if unknown5ea682ea * ext_call.return_data / 10000:
          require ext_code.size(rewardTokenAddress)
          call rewardTokenAddress.transfer(address to, uint256 tokens) with:
               gas gas_remaining wei
              args devAddr, unknown5ea682ea * ext_call.return_data / 10000
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'DexStrategyV4::_reinvest, dev'
      if not ext_call.return_data[0]:
          if not ext_call.return_data[0]:
              if unknown5ea682ea * ext_call.return_data / 10000 > ext_call.return_data[0]:
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              if 0 > ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) / 2 <= 0:
                  revert with 0, 
                              32,
                              50,
                              0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                              mem[662 len 14]
              require ext_code.size(unknownc89039c5Address)
              static call unknownc89039c5Address.0xdfe1681 with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[608] = ext_call.return_data[12 len 20]
              if rewardTokenAddress != mem[620 len 20]:
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              require ext_code.size(unknownc89039c5Address)
              static call unknownc89039c5Address.token1() with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[704] = ext_call.return_data[12 len 20]
              if rewardTokenAddress != mem[716 len 20]:
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              require ext_code.size(unknownf887ea40Address)
              call unknownf887ea40Address.0xe8e33700 with:
                   gas gas_remaining wei
                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 96
              if ext_call.return_data <= 0:
                  revert with 0, 
                              32,
                              34,
                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000))
          else:
              if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                  revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
              if unknown8aff733d * ext_call.return_data / 10000:
                  require ext_code.size(rewardTokenAddress)
                  call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                       gas gas_remaining wei
                      args caller, unknown8aff733d * ext_call.return_data / 10000
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if not ext_call.return_data[0]:
                      revert with 0, 'DexStrategyV4::_reinvest, reward'
              if unknown5ea682ea * ext_call.return_data / 10000 > ext_call.return_data[0]:
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              if 0 > ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              if unknown8aff733d * ext_call.return_data / 10000 > ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                  revert with 0, 
                              32,
                              50,
                              0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                              mem[662 len 14]
              require ext_code.size(unknownc89039c5Address)
              static call unknownc89039c5Address.0xdfe1681 with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[608] = ext_call.return_data[12 len 20]
              if rewardTokenAddress != mem[620 len 20]:
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              require ext_code.size(unknownc89039c5Address)
              static call unknownc89039c5Address.token1() with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[704] = ext_call.return_data[12 len 20]
              if rewardTokenAddress != mem[716 len 20]:
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              require ext_code.size(unknownf887ea40Address)
              call unknownf887ea40Address.0xe8e33700 with:
                   gas gas_remaining wei
                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 96
              if ext_call.return_data <= 0:
                  revert with 0, 
                              32,
                              34,
                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
      else:
          if unknown07677111 * ext_call.return_data / ext_call.return_dataunknown07677111:
              revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[261 len 31]
          if unknown07677111 * ext_call.return_data / 10000:
              require ext_code.size(rewardTokenAddress)
              call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                   gas gas_remaining wei
                  args owner, unknown07677111 * ext_call.return_data / 10000
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'DexStrategyV4::_reinvest, admin'
          if not ext_call.return_data[0]:
              if unknown5ea682ea * ext_call.return_data / 10000 > ext_call.return_data[0]:
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              if unknown07677111 * ext_call.return_data / 10000 > ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              if 0 > ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                  revert with 0, 
                              32,
                              50,
                              0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                              mem[662 len 14]
              require ext_code.size(unknownc89039c5Address)
              static call unknownc89039c5Address.0xdfe1681 with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[608] = ext_call.return_data[12 len 20]
              if rewardTokenAddress != mem[620 len 20]:
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              require ext_code.size(unknownc89039c5Address)
              static call unknownc89039c5Address.token1() with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[704] = ext_call.return_data[12 len 20]
              if rewardTokenAddress != mem[716 len 20]:
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              require ext_code.size(unknownf887ea40Address)
              call unknownf887ea40Address.0xe8e33700 with:
                   gas gas_remaining wei
                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 96
              if ext_call.return_data <= 0:
                  revert with 0, 
                              32,
                              34,
                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000))
          else:
              if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                  revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
              if unknown8aff733d * ext_call.return_data / 10000:
                  require ext_code.size(rewardTokenAddress)
                  call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                       gas gas_remaining wei
                      args caller, unknown8aff733d * ext_call.return_data / 10000
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if not ext_call.return_data[0]:
                      revert with 0, 'DexStrategyV4::_reinvest, reward'
              if unknown5ea682ea * ext_call.return_data / 10000 > ext_call.return_data[0]:
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              if unknown07677111 * ext_call.return_data / 10000 > ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              if unknown8aff733d * ext_call.return_data / 10000 > ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                  revert with 0, 
                              32,
                              50,
                              0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                              mem[662 len 14]
              require ext_code.size(unknownc89039c5Address)
              static call unknownc89039c5Address.0xdfe1681 with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[608] = ext_call.return_data[12 len 20]
              if rewardTokenAddress != mem[620 len 20]:
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              require ext_code.size(unknownc89039c5Address)
              static call unknownc89039c5Address.token1() with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[704] = ext_call.return_data[12 len 20]
              if rewardTokenAddress != mem[716 len 20]:
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              require ext_code.size(unknownf887ea40Address)
              call unknownf887ea40Address.0xe8e33700 with:
                   gas gas_remaining wei
                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 96
              if ext_call.return_data <= 0:
                  revert with 0, 
                              32,
                              34,
                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
  ('gt', ('ext_call.return_data', 64, 32), 0)
  require ext_code.size(stakingContractAddress)
  call stakingContractAddress.stake(uint256 stakeAmount) with:
       gas gas_remaining wei
      args ext_call.return_data[64]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  if ext_call.return_datatotalDeposits < totalDeposits:
      revert with 0, 'SafeMath: addition overflow'
  totalDeposits += ext_call.return_data[64]
  log 0xc7606d21: ext_call.return_data

def deposit(uint256 _amount) payable: 
  require calldata.size - 4 >= 32
  if not unknown3bdc6e72:
      if bool(unknownb52a321f) != 1:
          revert with 0, 'DexStrategyV4::_deposit'
      if not unknown789139bc:
          require ext_code.size(unknownc89039c5Address)
          call unknownc89039c5Address.transferFrom(address from, address to, uint256 tokens) with:
               gas gas_remaining wei
              args caller, this.address, _amount
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0]
          if _amount <= 0:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          34,
                          0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                          mem[198 len 30]
          require ext_code.size(stakingContractAddress)
          call stakingContractAddress.stake(uint256 stakeAmount) with:
               gas gas_remaining wei
              args _amount
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if not totalSupply:
              if _amount + totalSupply < totalSupply:
                  revert with 0, 'SafeMath: addition overflow'
              totalSupply += _amount
              if _amount + balanceOf[caller] < balanceOf[caller]:
                  revert with 0, 'SafeMath: addition overflow'
              balanceOf[caller] += _amount
              log Transfer(
                    address from=_amount,
                    address to=0,
                    uint256 tokens=caller)
          else:
              if totalDeposits * totalSupply / totalSupply != totalDeposits:
                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                              32,
                              33,
                              0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                              mem[197 len 31]
              if not totalDeposits * totalSupply:
                  if _amount + totalSupply < totalSupply:
                      revert with 0, 'SafeMath: addition overflow'
                  totalSupply += _amount
                  if _amount + balanceOf[caller] < balanceOf[caller]:
                      revert with 0, 'SafeMath: addition overflow'
                  balanceOf[caller] += _amount
                  log Transfer(
                        address from=_amount,
                        address to=0,
                        uint256 tokens=caller)
              else:
                  if not _amount:
                      if not totalDeposits:
                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      if (0 / totalDeposits) + totalSupply < totalSupply:
                          revert with 0, 'SafeMath: addition overflow'
                      totalSupply += 0 / totalDeposits
                      if (0 / totalDeposits) + balanceOf[caller] < balanceOf[caller]:
                          revert with 0, 'SafeMath: addition overflow'
                      balanceOf[caller] += 0 / totalDeposits
                      log Transfer(
                            address from=(0 / totalDeposits),
                            address to=0,
                            uint256 tokens=caller)
                  else:
                      if totalSupply * _amount / _amount != totalSupply:
                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                      32,
                                      33,
                                      0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                      mem[197 len 31]
                      if not totalDeposits:
                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      if (totalSupply * _amount / totalDeposits) + totalSupply < totalSupply:
                          revert with 0, 'SafeMath: addition overflow'
                      totalSupply += totalSupply * _amount / totalDeposits
                      if (totalSupply * _amount / totalDeposits) + balanceOf[caller] < balanceOf[caller]:
                          revert with 0, 'SafeMath: addition overflow'
                      balanceOf[caller] += totalSupply * _amount / totalDeposits
                      log Transfer(
                            address from=(totalSupply * _amount / totalDeposits),
                            address to=0,
                            uint256 tokens=caller)
          if _amount + totalDeposits < totalDeposits:
              revert with 0, 'SafeMath: addition overflow'
          totalDeposits += _amount
          log Deposit(
                address sender=_amount,
                uint256 value=caller)
          stop
      require ext_code.size(stakingContractAddress)
      static call stakingContractAddress.0x8cc262 with:
              gas gas_remaining wei
             args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data <= unknown789139bc:
          require ext_code.size(unknownc89039c5Address)
          call unknownc89039c5Address.transferFrom(address from, address to, uint256 tokens) with:
               gas gas_remaining wei
              args caller, this.address, _amount
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0]
          if _amount <= 0:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          34,
                          0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                          mem[198 len 30]
          require ext_code.size(stakingContractAddress)
          call stakingContractAddress.stake(uint256 stakeAmount) with:
               gas gas_remaining wei
              args _amount
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if not totalSupply:
              if _amount + totalSupply < totalSupply:
                  revert with 0, 'SafeMath: addition overflow'
              totalSupply += _amount
              if _amount + balanceOf[caller] < balanceOf[caller]:
                  revert with 0, 'SafeMath: addition overflow'
              balanceOf[caller] += _amount
              log Transfer(
                    address from=_amount,
                    address to=0,
                    uint256 tokens=caller)
          else:
              if totalDeposits * totalSupply / totalSupply != totalDeposits:
                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                              32,
                              33,
                              0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                              mem[197 len 31]
              if not totalDeposits * totalSupply:
                  if _amount + totalSupply < totalSupply:
                      revert with 0, 'SafeMath: addition overflow'
                  totalSupply += _amount
                  if _amount + balanceOf[caller] < balanceOf[caller]:
                      revert with 0, 'SafeMath: addition overflow'
                  balanceOf[caller] += _amount
                  log Transfer(
                        address from=_amount,
                        address to=0,
                        uint256 tokens=caller)
              else:
                  if not _amount:
                      if not totalDeposits:
                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      if (0 / totalDeposits) + totalSupply < totalSupply:
                          revert with 0, 'SafeMath: addition overflow'
                      totalSupply += 0 / totalDeposits
                      if (0 / totalDeposits) + balanceOf[caller] < balanceOf[caller]:
                          revert with 0, 'SafeMath: addition overflow'
                      balanceOf[caller] += 0 / totalDeposits
                      log Transfer(
                            address from=(0 / totalDeposits),
                            address to=0,
                            uint256 tokens=caller)
                  else:
                      if totalSupply * _amount / _amount != totalSupply:
                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                      32,
                                      33,
                                      0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                      mem[197 len 31]
                      if not totalDeposits:
                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      if (totalSupply * _amount / totalDeposits) + totalSupply < totalSupply:
                          revert with 0, 'SafeMath: addition overflow'
                      totalSupply += totalSupply * _amount / totalDeposits
                      if (totalSupply * _amount / totalDeposits) + balanceOf[caller] < balanceOf[caller]:
                          revert with 0, 'SafeMath: addition overflow'
                      balanceOf[caller] += totalSupply * _amount / totalDeposits
                      log Transfer(
                            address from=(totalSupply * _amount / totalDeposits),
                            address to=0,
                            uint256 tokens=caller)
          if _amount + totalDeposits < totalDeposits:
              revert with 0, 'SafeMath: addition overflow'
          totalDeposits += _amount
          log Deposit(
                address sender=_amount,
                uint256 value=caller)
          stop
      require ext_code.size(stakingContractAddress)
      call stakingContractAddress.getReward() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      if not ext_call.return_data[0]:
          if not ext_call.return_data[0]:
              if not ext_call.return_data[0]:
                  if 0 <= ext_call.return_data[0]:
                      if ext_call.return_data / 2 <= 0:
                          revert with 0, 
                                      32,
                                      50,
                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                      mem[662 len 14]
                      require ext_code.size(unknownc89039c5Address)
                      static call unknownc89039c5Address.0xdfe1681 with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mem[608] = ext_call.return_data[12 len 20]
                      if rewardTokenAddress == mem[620 len 20]:
                          require ext_code.size(unknownc89039c5Address)
                          static call unknownc89039c5Address.token1() with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mem[704] = ext_call.return_data[12 len 20]
                          if rewardTokenAddress == mem[716 len 20]:
                              require ext_code.size(unknownf887ea40Address)
                              call unknownf887ea40Address.0xe8e33700 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataaddr(this.address), block.timestamp
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 96
                              if ext_call.return_data <= 0:
                                  revert with 0, 
                                              32,
                                              34,
                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                              Mask(239, 1, ext_call.return_data[0])
                              require ext_code.size(stakingContractAddress)
                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                   gas gas_remaining wei
                                  args ext_call.return_data[64]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              if ext_call.return_datatotalDeposits < totalDeposits:
                                  revert with 0, 'SafeMath: addition overflow'
                              totalDeposits += ext_call.return_data[64]
                              log 0xc7606d21: ext_call.return_data
              else:
                  if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                      revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                  if not unknown8aff733d * ext_call.return_data / 10000:
                      if 0 <= ext_call.return_data[0]:
                          if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                  revert with 0, 
                                              32,
                                              50,
                                              0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                              mem[662 len 14]
                              require ext_code.size(unknownc89039c5Address)
                              static call unknownc89039c5Address.0xdfe1681 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[608] = ext_call.return_data[12 len 20]
                              if rewardTokenAddress == mem[620 len 20]:
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.token1() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[704] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[716 len 20]:
                                      require ext_code.size(unknownf887ea40Address)
                                      call unknownf887ea40Address.0xe8e33700 with:
                                           gas gas_remaining wei
                                          args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 96
                                      if ext_call.return_data <= 0:
                                          revert with 0, 
                                                      32,
                                                      34,
                                                      0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                      Mask(239, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000))
                                      require ext_code.size(stakingContractAddress)
                                      call stakingContractAddress.stake(uint256 stakeAmount) with:
                                           gas gas_remaining wei
                                          args ext_call.return_data[64]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      if ext_call.return_datatotalDeposits < totalDeposits:
                                          revert with 0, 'SafeMath: addition overflow'
                                      totalDeposits += ext_call.return_data[64]
                                      log 0xc7606d21: ext_call.return_data
                  else:
                      require ext_code.size(rewardTokenAddress)
                      call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                           gas gas_remaining wei
                          args caller, unknown8aff733d * ext_call.return_data / 10000
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not ext_call.return_data[0]:
                          revert with 0, 'DexStrategyV4::_reinvest, reward'
                      if 0 <= ext_call.return_data[0]:
                          if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                  revert with 0, 
                                              32,
                                              50,
                                              0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                              mem[662 len 14]
                              require ext_code.size(unknownc89039c5Address)
                              static call unknownc89039c5Address.0xdfe1681 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[608] = ext_call.return_data[12 len 20]
                              if rewardTokenAddress == mem[620 len 20]:
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.token1() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[704] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[716 len 20]:
                                      require ext_code.size(unknownf887ea40Address)
                                      call unknownf887ea40Address.0xe8e33700 with:
                                           gas gas_remaining wei
                                          args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 96
                                      if ext_call.return_data <= 0:
                                          revert with 0, 
                                                      32,
                                                      34,
                                                      0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                      Mask(239, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000))
                                      require ext_code.size(stakingContractAddress)
                                      call stakingContractAddress.stake(uint256 stakeAmount) with:
                                           gas gas_remaining wei
                                          args ext_call.return_data[64]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
          else:
              if unknown07677111 * ext_call.return_data / ext_call.return_dataunknown07677111:
                  revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[261 len 31]
              if not unknown07677111 * ext_call.return_data / 10000:
                  if not ext_call.return_data[0]:
                      if 0 <= ext_call.return_data[0]:
                          if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                  if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                      revert with 0, 
                                                  32,
                                                  50,
                                                  0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                  mem[662 len 14]
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.0xdfe1681 with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[608] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[620 len 20]:
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.token1() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[704] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[716 len 20]:
                                          require ext_code.size(unknownf887ea40Address)
                                          call unknownf887ea40Address.0xe8e33700 with:
                                               gas gas_remaining wei
                                              args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 96
                                          if ext_call.return_data <= 0:
                                              revert with 0, 
                                                          32,
                                                          34,
                                                          0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                          Mask(239, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000))
                                          require ext_code.size(stakingContractAddress)
                                          call stakingContractAddress.stake(uint256 stakeAmount) with:
                                               gas gas_remaining wei
                                              args ext_call.return_data[64]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          if ext_call.return_datatotalDeposits < totalDeposits:
                                              revert with 0, 'SafeMath: addition overflow'
                                          totalDeposits += ext_call.return_data[64]
                                          log 0xc7606d21: ext_call.return_data
                  else:
                      if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                          revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                      if not unknown8aff733d * ext_call.return_data / 10000:
                          if 0 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              if ext_call.return_datatotalDeposits < totalDeposits:
                                                  revert with 0, 'SafeMath: addition overflow'
                                              totalDeposits += ext_call.return_data[64]
                                              log 0xc7606d21: ext_call.return_data
                      else:
                          require ext_code.size(rewardTokenAddress)
                          call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                               gas gas_remaining wei
                              args caller, unknown8aff733d * ext_call.return_data / 10000
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              revert with 0, 'DexStrategyV4::_reinvest, reward'
                          if 0 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  require ext_code.size(rewardTokenAddress)
                  call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                       gas gas_remaining wei
                      args owner, unknown07677111 * ext_call.return_data / 10000
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if not ext_call.return_data[0]:
                      revert with 0, 'DexStrategyV4::_reinvest, admin'
                  if not ext_call.return_data[0]:
                      if 0 <= ext_call.return_data[0]:
                          if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                  if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                      revert with 0, 
                                                  32,
                                                  50,
                                                  0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                  mem[662 len 14]
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.0xdfe1681 with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[608] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[620 len 20]:
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.token1() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[704] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[716 len 20]:
                                          require ext_code.size(unknownf887ea40Address)
                                          call unknownf887ea40Address.0xe8e33700 with:
                                               gas gas_remaining wei
                                              args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 96
                                          if ext_call.return_data <= 0:
                                              revert with 0, 
                                                          32,
                                                          34,
                                                          0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                          Mask(239, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000))
                                          require ext_code.size(stakingContractAddress)
                                          call stakingContractAddress.stake(uint256 stakeAmount) with:
                                               gas gas_remaining wei
                                              args ext_call.return_data[64]
                  else:
                      if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                          revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                      if not unknown8aff733d * ext_call.return_data / 10000:
                          if 0 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                      else:
                          require ext_code.size(rewardTokenAddress)
                          call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                               gas gas_remaining wei
                              args caller, unknown8aff733d * ext_call.return_data / 10000
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              revert with 0, 'DexStrategyV4::_reinvest, reward'
                          if 0 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
      else:
          if unknown5ea682ea * ext_call.return_data / ext_call.return_dataunknown5ea682ea:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          33,
                          0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                          mem[197 len 31]
          if not unknown5ea682ea * ext_call.return_data / 10000:
              if not ext_call.return_data[0]:
                  if not ext_call.return_data[0]:
                      if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                          if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                              if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) / 2 <= 0:
                                  revert with 0, 
                                              32,
                                              50,
                                              0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                              mem[662 len 14]
                              require ext_code.size(unknownc89039c5Address)
                              static call unknownc89039c5Address.0xdfe1681 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[608] = ext_call.return_data[12 len 20]
                              if rewardTokenAddress == mem[620 len 20]:
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.token1() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[704] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[716 len 20]:
                                      require ext_code.size(unknownf887ea40Address)
                                      call unknownf887ea40Address.0xe8e33700 with:
                                           gas gas_remaining wei
                                          args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 96
                                      if ext_call.return_data <= 0:
                                          revert with 0, 
                                                      32,
                                                      34,
                                                      0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                      Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000))
                                      require ext_code.size(stakingContractAddress)
                                      call stakingContractAddress.stake(uint256 stakeAmount) with:
                                           gas gas_remaining wei
                                          args ext_call.return_data[64]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      if ext_call.return_datatotalDeposits < totalDeposits:
                                          revert with 0, 'SafeMath: addition overflow'
                                      totalDeposits += ext_call.return_data[64]
                                      log 0xc7606d21: ext_call.return_data
                  else:
                      if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                          revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                      if not unknown8aff733d * ext_call.return_data / 10000:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              if ext_call.return_datatotalDeposits < totalDeposits:
                                                  revert with 0, 'SafeMath: addition overflow'
                                              totalDeposits += ext_call.return_data[64]
                                              log 0xc7606d21: ext_call.return_data
                      else:
                          require ext_code.size(rewardTokenAddress)
                          call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                               gas gas_remaining wei
                              args caller, unknown8aff733d * ext_call.return_data / 10000
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              revert with 0, 'DexStrategyV4::_reinvest, reward'
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  if unknown07677111 * ext_call.return_data / ext_call.return_dataunknown07677111:
                      revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[261 len 31]
                  if not unknown07677111 * ext_call.return_data / 10000:
                      if not ext_call.return_data[0]:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              if ext_call.return_datatotalDeposits < totalDeposits:
                                                  revert with 0, 'SafeMath: addition overflow'
                                              totalDeposits += ext_call.return_data[64]
                                              log 0xc7606d21: ext_call.return_data
                      else:
                          if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                              revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                          if not unknown8aff733d * ext_call.return_data / 10000:
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >= 96
                                                  if ext_call.return_data <= 0:
                                                      revert with 0, 
                                                                  32,
                                                                  34,
                                                                  0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                                  Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                                  require ext_code.size(stakingContractAddress)
                                                  call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                       gas gas_remaining wei
                                                      args ext_call.return_data[64]
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  if ext_call.return_datatotalDeposits < totalDeposits:
                                                      revert with 0, 'SafeMath: addition overflow'
                          else:
                              require ext_code.size(rewardTokenAddress)
                              call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                                   gas gas_remaining wei
                                  args caller, unknown8aff733d * ext_call.return_data / 10000
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not ext_call.return_data[0]:
                                  revert with 0, 'DexStrategyV4::_reinvest, reward'
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >= 96
                                                  if ext_call.return_data <= 0:
                                                      revert with 0, 
                                                                  32,
                                                                  34,
                                                                  0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                                  Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                                  require ext_code.size(stakingContractAddress)
                                                  call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                       gas gas_remaining wei
                                                      args ext_call.return_data[64]
                  else:
                      require ext_code.size(rewardTokenAddress)
                      call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                           gas gas_remaining wei
                          args owner, unknown07677111 * ext_call.return_data / 10000
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not ext_call.return_data[0]:
                          revert with 0, 'DexStrategyV4::_reinvest, admin'
                      if not ext_call.return_data[0]:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000))
                      else:
                          if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                              revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                          if not unknown8aff733d * ext_call.return_data / 10000:
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >= 96
                          else:
                              require ext_code.size(rewardTokenAddress)
                              call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                                   gas gas_remaining wei
                                  args caller, unknown8aff733d * ext_call.return_data / 10000
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not ext_call.return_data[0]:
                                  revert with 0, 'DexStrategyV4::_reinvest, reward'
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
          else:
              require ext_code.size(rewardTokenAddress)
              call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                   gas gas_remaining wei
                  args devAddr, unknown5ea682ea * ext_call.return_data / 10000
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'DexStrategyV4::_reinvest, dev'
              if not ext_call.return_data[0]:
                  if not ext_call.return_data[0]:
                      if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                          if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                              if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) / 2 <= 0:
                                  revert with 0, 
                                              32,
                                              50,
                                              0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                              mem[662 len 14]
                              require ext_code.size(unknownc89039c5Address)
                              static call unknownc89039c5Address.0xdfe1681 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[608] = ext_call.return_data[12 len 20]
                              if rewardTokenAddress == mem[620 len 20]:
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.token1() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[704] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[716 len 20]:
                                      require ext_code.size(unknownf887ea40Address)
                                      call unknownf887ea40Address.0xe8e33700 with:
                                           gas gas_remaining wei
                                          args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 96
                                      if ext_call.return_data <= 0:
                                          revert with 0, 
                                                      32,
                                                      34,
                                                      0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                      Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000))
                                      require ext_code.size(stakingContractAddress)
                                      call stakingContractAddress.stake(uint256 stakeAmount) with:
                                           gas gas_remaining wei
                                          args ext_call.return_data[64]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                  else:
                      if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                          revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                      if not unknown8aff733d * ext_call.return_data / 10000:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                      else:
                          require ext_code.size(rewardTokenAddress)
                          call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                               gas gas_remaining wei
                              args caller, unknown8aff733d * ext_call.return_data / 10000
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              revert with 0, 'DexStrategyV4::_reinvest, reward'
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
              else:
                  if unknown07677111 * ext_call.return_data / ext_call.return_dataunknown07677111:
                      revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[261 len 31]
                  if not unknown07677111 * ext_call.return_data / 10000:
                      if not ext_call.return_data[0]:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                      else:
                          if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                              revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                          if not unknown8aff733d * ext_call.return_data / 10000:
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >= 96
                                                  if ext_call.return_data <= 0:
                                                      revert with 0, 
                                                                  32,
                                                                  34,
                                                                  0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                                  Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                                  require ext_code.size(stakingContractAddress)
                                                  call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                       gas gas_remaining wei
                                                      args ext_call.return_data[64]
                          else:
                              require ext_code.size(rewardTokenAddress)
                              call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                                   gas gas_remaining wei
                                  args caller, unknown8aff733d * ext_call.return_data / 10000
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not ext_call.return_data[0]:
                                  revert with 0, 'DexStrategyV4::_reinvest, reward'
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >= 96
                  else:
                      require ext_code.size(rewardTokenAddress)
                      call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                           gas gas_remaining wei
                          args owner, unknown07677111 * ext_call.return_data / 10000
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not ext_call.return_data[0]:
                          revert with 0, 'DexStrategyV4::_reinvest, admin'
                      if not ext_call.return_data[0]:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                      else:
                          if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                              revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                          if not unknown8aff733d * ext_call.return_data / 10000:
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                          else:
                              require ext_code.size(rewardTokenAddress)
                              call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                                   gas gas_remaining wei
                                  args caller, unknown8aff733d * ext_call.return_data / 10000
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not ext_call.return_data[0]:
                                  revert with 0, 'DexStrategyV4::_reinvest, reward'
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
  else:
      if bool(stor8[caller]) != 1:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      32,
                      46,
                      0x735065726d697373696f6e65643a3a6f6e6c79416c6c6f7765644465706f736974732c206e6f7420616c6c6f7765,
                      mem[210 len 18]
      if bool(unknownb52a321f) != 1:
          revert with 0, 'DexStrategyV4::_deposit'
      if not unknown789139bc:
          require ext_code.size(unknownc89039c5Address)
          call unknownc89039c5Address.transferFrom(address from, address to, uint256 tokens) with:
               gas gas_remaining wei
              args caller, this.address, _amount
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0]
          if _amount <= 0:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          34,
                          0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                          mem[198 len 30]
          require ext_code.size(stakingContractAddress)
          call stakingContractAddress.stake(uint256 stakeAmount) with:
               gas gas_remaining wei
              args _amount
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if not totalSupply:
              if _amount + totalSupply < totalSupply:
                  revert with 0, 'SafeMath: addition overflow'
              totalSupply += _amount
              if _amount + balanceOf[caller] < balanceOf[caller]:
                  revert with 0, 'SafeMath: addition overflow'
              balanceOf[caller] += _amount
              log Transfer(
                    address from=_amount,
                    address to=0,
                    uint256 tokens=caller)
          else:
              if totalDeposits * totalSupply / totalSupply != totalDeposits:
                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                              32,
                              33,
                              0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                              mem[197 len 31]
              if not totalDeposits * totalSupply:
                  if _amount + totalSupply < totalSupply:
                      revert with 0, 'SafeMath: addition overflow'
                  totalSupply += _amount
                  if _amount + balanceOf[caller] < balanceOf[caller]:
                      revert with 0, 'SafeMath: addition overflow'
                  balanceOf[caller] += _amount
                  log Transfer(
                        address from=_amount,
                        address to=0,
                        uint256 tokens=caller)
              else:
                  if not _amount:
                      if not totalDeposits:
                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      if (0 / totalDeposits) + totalSupply < totalSupply:
                          revert with 0, 'SafeMath: addition overflow'
                      totalSupply += 0 / totalDeposits
                      if (0 / totalDeposits) + balanceOf[caller] < balanceOf[caller]:
                          revert with 0, 'SafeMath: addition overflow'
                      balanceOf[caller] += 0 / totalDeposits
                      log Transfer(
                            address from=(0 / totalDeposits),
                            address to=0,
                            uint256 tokens=caller)
                  else:
                      if totalSupply * _amount / _amount != totalSupply:
                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                      32,
                                      33,
                                      0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                      mem[197 len 31]
                      if not totalDeposits:
                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      if (totalSupply * _amount / totalDeposits) + totalSupply < totalSupply:
                          revert with 0, 'SafeMath: addition overflow'
                      totalSupply += totalSupply * _amount / totalDeposits
                      if (totalSupply * _amount / totalDeposits) + balanceOf[caller] < balanceOf[caller]:
                          revert with 0, 'SafeMath: addition overflow'
                      balanceOf[caller] += totalSupply * _amount / totalDeposits
                      log Transfer(
                            address from=(totalSupply * _amount / totalDeposits),
                            address to=0,
                            uint256 tokens=caller)
          if _amount + totalDeposits < totalDeposits:
              revert with 0, 'SafeMath: addition overflow'
          totalDeposits += _amount
          log Deposit(
                address sender=_amount,
                uint256 value=caller)
          stop
      require ext_code.size(stakingContractAddress)
      static call stakingContractAddress.0x8cc262 with:
              gas gas_remaining wei
             args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data <= unknown789139bc:
          require ext_code.size(unknownc89039c5Address)
          call unknownc89039c5Address.transferFrom(address from, address to, uint256 tokens) with:
               gas gas_remaining wei
              args caller, this.address, _amount
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0]
          if _amount <= 0:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          34,
                          0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                          mem[198 len 30]
          require ext_code.size(stakingContractAddress)
          call stakingContractAddress.stake(uint256 stakeAmount) with:
               gas gas_remaining wei
              args _amount
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if not totalSupply:
              if _amount + totalSupply < totalSupply:
                  revert with 0, 'SafeMath: addition overflow'
              totalSupply += _amount
              if _amount + balanceOf[caller] < balanceOf[caller]:
                  revert with 0, 'SafeMath: addition overflow'
              balanceOf[caller] += _amount
              log Transfer(
                    address from=_amount,
                    address to=0,
                    uint256 tokens=caller)
          else:
              if totalDeposits * totalSupply / totalSupply != totalDeposits:
                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                              32,
                              33,
                              0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                              mem[197 len 31]
              if not totalDeposits * totalSupply:
                  if _amount + totalSupply < totalSupply:
                      revert with 0, 'SafeMath: addition overflow'
                  totalSupply += _amount
                  if _amount + balanceOf[caller] < balanceOf[caller]:
                      revert with 0, 'SafeMath: addition overflow'
                  balanceOf[caller] += _amount
                  log Transfer(
                        address from=_amount,
                        address to=0,
                        uint256 tokens=caller)
              else:
                  if not _amount:
                      if not totalDeposits:
                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      if (0 / totalDeposits) + totalSupply < totalSupply:
                          revert with 0, 'SafeMath: addition overflow'
                      totalSupply += 0 / totalDeposits
                      if (0 / totalDeposits) + balanceOf[caller] < balanceOf[caller]:
                          revert with 0, 'SafeMath: addition overflow'
                      balanceOf[caller] += 0 / totalDeposits
                      log Transfer(
                            address from=(0 / totalDeposits),
                            address to=0,
                            uint256 tokens=caller)
                  else:
                      if totalSupply * _amount / _amount != totalSupply:
                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                      32,
                                      33,
                                      0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                      mem[197 len 31]
                      if not totalDeposits:
                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      if (totalSupply * _amount / totalDeposits) + totalSupply < totalSupply:
                          revert with 0, 'SafeMath: addition overflow'
                      totalSupply += totalSupply * _amount / totalDeposits
                      if (totalSupply * _amount / totalDeposits) + balanceOf[caller] < balanceOf[caller]:
                          revert with 0, 'SafeMath: addition overflow'
                      balanceOf[caller] += totalSupply * _amount / totalDeposits
                      log Transfer(
                            address from=(totalSupply * _amount / totalDeposits),
                            address to=0,
                            uint256 tokens=caller)
          if _amount + totalDeposits < totalDeposits:
              revert with 0, 'SafeMath: addition overflow'
          totalDeposits += _amount
          log Deposit(
                address sender=_amount,
                uint256 value=caller)
          stop
      require ext_code.size(stakingContractAddress)
      call stakingContractAddress.getReward() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      if not ext_call.return_data[0]:
          if not ext_call.return_data[0]:
              if not ext_call.return_data[0]:
                  if 0 <= ext_call.return_data[0]:
                      if ext_call.return_data / 2 <= 0:
                          revert with 0, 
                                      32,
                                      50,
                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                      mem[662 len 14]
                      require ext_code.size(unknownc89039c5Address)
                      static call unknownc89039c5Address.0xdfe1681 with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mem[608] = ext_call.return_data[12 len 20]
                      if rewardTokenAddress == mem[620 len 20]:
                          require ext_code.size(unknownc89039c5Address)
                          static call unknownc89039c5Address.token1() with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mem[704] = ext_call.return_data[12 len 20]
                          if rewardTokenAddress == mem[716 len 20]:
                              require ext_code.size(unknownf887ea40Address)
                              call unknownf887ea40Address.0xe8e33700 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataaddr(this.address), block.timestamp
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 96
                              if ext_call.return_data <= 0:
                                  revert with 0, 
                                              32,
                                              34,
                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                              Mask(239, 1, ext_call.return_data[0])
                              require ext_code.size(stakingContractAddress)
                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                   gas gas_remaining wei
                                  args ext_call.return_data[64]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              if ext_call.return_datatotalDeposits < totalDeposits:
                                  revert with 0, 'SafeMath: addition overflow'
                              totalDeposits += ext_call.return_data[64]
                              log 0xc7606d21: ext_call.return_data
              else:
                  if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                      revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                  if not unknown8aff733d * ext_call.return_data / 10000:
                      if 0 <= ext_call.return_data[0]:
                          if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                  revert with 0, 
                                              32,
                                              50,
                                              0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                              mem[662 len 14]
                              require ext_code.size(unknownc89039c5Address)
                              static call unknownc89039c5Address.0xdfe1681 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[608] = ext_call.return_data[12 len 20]
                              if rewardTokenAddress == mem[620 len 20]:
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.token1() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[704] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[716 len 20]:
                                      require ext_code.size(unknownf887ea40Address)
                                      call unknownf887ea40Address.0xe8e33700 with:
                                           gas gas_remaining wei
                                          args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 96
                                      if ext_call.return_data <= 0:
                                          revert with 0, 
                                                      32,
                                                      34,
                                                      0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                      Mask(239, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000))
                                      require ext_code.size(stakingContractAddress)
                                      call stakingContractAddress.stake(uint256 stakeAmount) with:
                                           gas gas_remaining wei
                                          args ext_call.return_data[64]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      if ext_call.return_datatotalDeposits < totalDeposits:
                                          revert with 0, 'SafeMath: addition overflow'
                                      totalDeposits += ext_call.return_data[64]
                                      log 0xc7606d21: ext_call.return_data
                  else:
                      require ext_code.size(rewardTokenAddress)
                      call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                           gas gas_remaining wei
                          args caller, unknown8aff733d * ext_call.return_data / 10000
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not ext_call.return_data[0]:
                          revert with 0, 'DexStrategyV4::_reinvest, reward'
                      if 0 <= ext_call.return_data[0]:
                          if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                  revert with 0, 
                                              32,
                                              50,
                                              0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                              mem[662 len 14]
                              require ext_code.size(unknownc89039c5Address)
                              static call unknownc89039c5Address.0xdfe1681 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[608] = ext_call.return_data[12 len 20]
                              if rewardTokenAddress == mem[620 len 20]:
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.token1() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[704] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[716 len 20]:
                                      require ext_code.size(unknownf887ea40Address)
                                      call unknownf887ea40Address.0xe8e33700 with:
                                           gas gas_remaining wei
                                          args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 96
                                      if ext_call.return_data <= 0:
                                          revert with 0, 
                                                      32,
                                                      34,
                                                      0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                      Mask(239, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000))
                                      require ext_code.size(stakingContractAddress)
                                      call stakingContractAddress.stake(uint256 stakeAmount) with:
                                           gas gas_remaining wei
                                          args ext_call.return_data[64]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
          else:
              if unknown07677111 * ext_call.return_data / ext_call.return_dataunknown07677111:
                  revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[261 len 31]
              if not unknown07677111 * ext_call.return_data / 10000:
                  if not ext_call.return_data[0]:
                      if 0 <= ext_call.return_data[0]:
                          if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                  if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                      revert with 0, 
                                                  32,
                                                  50,
                                                  0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                  mem[662 len 14]
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.0xdfe1681 with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[608] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[620 len 20]:
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.token1() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[704] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[716 len 20]:
                                          require ext_code.size(unknownf887ea40Address)
                                          call unknownf887ea40Address.0xe8e33700 with:
                                               gas gas_remaining wei
                                              args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 96
                                          if ext_call.return_data <= 0:
                                              revert with 0, 
                                                          32,
                                                          34,
                                                          0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                          Mask(239, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000))
                                          require ext_code.size(stakingContractAddress)
                                          call stakingContractAddress.stake(uint256 stakeAmount) with:
                                               gas gas_remaining wei
                                              args ext_call.return_data[64]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          if ext_call.return_datatotalDeposits < totalDeposits:
                                              revert with 0, 'SafeMath: addition overflow'
                                          totalDeposits += ext_call.return_data[64]
                                          log 0xc7606d21: ext_call.return_data
                  else:
                      if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                          revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                      if not unknown8aff733d * ext_call.return_data / 10000:
                          if 0 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              if ext_call.return_datatotalDeposits < totalDeposits:
                                                  revert with 0, 'SafeMath: addition overflow'
                      else:
                          require ext_code.size(rewardTokenAddress)
                          call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                               gas gas_remaining wei
                              args caller, unknown8aff733d * ext_call.return_data / 10000
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              revert with 0, 'DexStrategyV4::_reinvest, reward'
                          if 0 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
              else:
                  require ext_code.size(rewardTokenAddress)
                  call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                       gas gas_remaining wei
                      args owner, unknown07677111 * ext_call.return_data / 10000
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if not ext_call.return_data[0]:
                      revert with 0, 'DexStrategyV4::_reinvest, admin'
                  if not ext_call.return_data[0]:
                      if 0 <= ext_call.return_data[0]:
                          if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                  if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                      revert with 0, 
                                                  32,
                                                  50,
                                                  0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                  mem[662 len 14]
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.0xdfe1681 with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[608] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[620 len 20]:
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.token1() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[704] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[716 len 20]:
                                          require ext_code.size(unknownf887ea40Address)
                                          call unknownf887ea40Address.0xe8e33700 with:
                                               gas gas_remaining wei
                                              args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 96
                                          if ext_call.return_data <= 0:
                                              revert with 0, 
                                                          32,
                                                          34,
                                                          0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                          Mask(239, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000))
                  else:
                      if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                          revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                      if not unknown8aff733d * ext_call.return_data / 10000:
                          if 0 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                      else:
                          require ext_code.size(rewardTokenAddress)
                          call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                               gas gas_remaining wei
                              args caller, unknown8aff733d * ext_call.return_data / 10000
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              revert with 0, 'DexStrategyV4::_reinvest, reward'
                          if 0 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
      else:
          if unknown5ea682ea * ext_call.return_data / ext_call.return_dataunknown5ea682ea:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          33,
                          0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                          mem[197 len 31]
          if not unknown5ea682ea * ext_call.return_data / 10000:
              if ext_call.return_data[0]:
                  if unknown07677111 * ext_call.return_data / ext_call.return_dataunknown07677111:
                      revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[261 len 31]
                  if not unknown07677111 * ext_call.return_data / 10000:
                      if not ext_call.return_data[0]:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              if ext_call.return_datatotalDeposits < totalDeposits:
                                                  revert with 0, 'SafeMath: addition overflow'
                      else:
                          if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                              revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                          if not unknown8aff733d * ext_call.return_data / 10000:
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >= 96
                                                  if ext_call.return_data <= 0:
                                                      revert with 0, 
                                                                  32,
                                                                  34,
                                                                  0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                                  Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                                  require ext_code.size(stakingContractAddress)
                                                  call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                       gas gas_remaining wei
                                                      args ext_call.return_data[64]
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require ext_code.size(rewardTokenAddress)
                              call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                                   gas gas_remaining wei
                                  args caller, unknown8aff733d * ext_call.return_data / 10000
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not ext_call.return_data[0]:
                                  revert with 0, 'DexStrategyV4::_reinvest, reward'
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >= 96
                                                  if ext_call.return_data <= 0:
                                                      revert with 0, 
                                                                  32,
                                                                  34,
                                                                  0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                                  Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                  else:
                      require ext_code.size(rewardTokenAddress)
                      call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                           gas gas_remaining wei
                          args owner, unknown07677111 * ext_call.return_data / 10000
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not ext_call.return_data[0]:
                          revert with 0, 'DexStrategyV4::_reinvest, admin'
                      if not ext_call.return_data[0]:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                      else:
                          if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                              revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                          if not unknown8aff733d * ext_call.return_data / 10000:
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >= 96
                          else:
                              require ext_code.size(rewardTokenAddress)
                              call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                                   gas gas_remaining wei
                                  args caller, unknown8aff733d * ext_call.return_data / 10000
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not ext_call.return_data[0]:
                                  revert with 0, 'DexStrategyV4::_reinvest, reward'
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
              else:
                  if not ext_call.return_data[0]:
                      if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                          if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                              if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) / 2 <= 0:
                                  revert with 0, 
                                              32,
                                              50,
                                              0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                              mem[662 len 14]
                              require ext_code.size(unknownc89039c5Address)
                              static call unknownc89039c5Address.0xdfe1681 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[608] = ext_call.return_data[12 len 20]
                              if rewardTokenAddress == mem[620 len 20]:
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.token1() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[704] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[716 len 20]:
                                      require ext_code.size(unknownf887ea40Address)
                                      call unknownf887ea40Address.0xe8e33700 with:
                                           gas gas_remaining wei
                                          args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 96
                                      if ext_call.return_data <= 0:
                                          revert with 0, 
                                                      32,
                                                      34,
                                                      0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                      Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000))
                                      require ext_code.size(stakingContractAddress)
                                      call stakingContractAddress.stake(uint256 stakeAmount) with:
                                           gas gas_remaining wei
                                          args ext_call.return_data[64]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      if ext_call.return_datatotalDeposits < totalDeposits:
                                          revert with 0, 'SafeMath: addition overflow'
                                      totalDeposits += ext_call.return_data[64]
                                      log 0xc7606d21: ext_call.return_data
                  else:
                      if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                          revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                      if not unknown8aff733d * ext_call.return_data / 10000:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              if ext_call.return_datatotalDeposits < totalDeposits:
                                                  revert with 0, 'SafeMath: addition overflow'
                      else:
                          require ext_code.size(rewardTokenAddress)
                          call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                               gas gas_remaining wei
                              args caller, unknown8aff733d * ext_call.return_data / 10000
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              revert with 0, 'DexStrategyV4::_reinvest, reward'
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
          else:
              require ext_code.size(rewardTokenAddress)
              call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                   gas gas_remaining wei
                  args devAddr, unknown5ea682ea * ext_call.return_data / 10000
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'DexStrategyV4::_reinvest, dev'
              if not ext_call.return_data[0]:
                  if not ext_call.return_data[0]:
                      if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                          if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                              if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) / 2 <= 0:
                                  revert with 0, 
                                              32,
                                              50,
                                              0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                              mem[662 len 14]
                              require ext_code.size(unknownc89039c5Address)
                              static call unknownc89039c5Address.0xdfe1681 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[608] = ext_call.return_data[12 len 20]
                              if rewardTokenAddress == mem[620 len 20]:
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.token1() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[704] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[716 len 20]:
                                      require ext_code.size(unknownf887ea40Address)
                                      call unknownf887ea40Address.0xe8e33700 with:
                                           gas gas_remaining wei
                                          args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 96
                                      if ext_call.return_data <= 0:
                                          revert with 0, 
                                                      32,
                                                      34,
                                                      0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                      Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000))
                                      require ext_code.size(stakingContractAddress)
                                      call stakingContractAddress.stake(uint256 stakeAmount) with:
                                           gas gas_remaining wei
                                          args ext_call.return_data[64]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                  else:
                      if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                          revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                      if not unknown8aff733d * ext_call.return_data / 10000:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                      else:
                          require ext_code.size(rewardTokenAddress)
                          call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                               gas gas_remaining wei
                              args caller, unknown8aff733d * ext_call.return_data / 10000
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              revert with 0, 'DexStrategyV4::_reinvest, reward'
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
              else:
                  if unknown07677111 * ext_call.return_data / ext_call.return_dataunknown07677111:
                      revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[261 len 31]
                  if unknown07677111 * ext_call.return_data / 10000:
                      require ext_code.size(rewardTokenAddress)
                      call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                           gas gas_remaining wei
                          args owner, unknown07677111 * ext_call.return_data / 10000
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not ext_call.return_data[0]:
                          revert with 0, 'DexStrategyV4::_reinvest, admin'
                      if not ext_call.return_data[0]:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                      else:
                          if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                              revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                          if not unknown8aff733d * ext_call.return_data / 10000:
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                          else:
                              require ext_code.size(rewardTokenAddress)
                              call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                                   gas gas_remaining wei
                                  args caller, unknown8aff733d * ext_call.return_data / 10000
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not ext_call.return_data[0]:
                                  revert with 0, 'DexStrategyV4::_reinvest, reward'
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                  else:
                      if not ext_call.return_data[0]:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                      else:
                          if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                              revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                          if not unknown8aff733d * ext_call.return_data / 10000:
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >= 96
                                                  if ext_call.return_data <= 0:
                                                      revert with 0, 
                                                                  32,
                                                                  34,
                                                                  0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                                  Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                          else:
                              require ext_code.size(rewardTokenAddress)
                              call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                                   gas gas_remaining wei
                                  args caller, unknown8aff733d * ext_call.return_data / 10000
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not ext_call.return_data[0]:
                                  revert with 0, 'DexStrategyV4::_reinvest, reward'
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)

def unknown4a970be7(uint256 _param1, uint256 _param2, uint8 _param3, uint256 _param4, uint256 _param5) payable: 
  require calldata.size - 4 >= 160
  require ext_code.size(unknownc89039c5Address)
  call unknownc89039c5Address.0xd505accf with:
       gas gas_remaining wei
      args 0, uint32(caller), this.address, _param1, _param2, _param3 << 248, _param4, _param5
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  if not unknown3bdc6e72:
      if bool(unknownb52a321f) != 1:
          revert with 0, 'DexStrategyV4::_deposit'
      if not unknown789139bc:
          require ext_code.size(unknownc89039c5Address)
          call unknownc89039c5Address.transferFrom(address from, address to, uint256 tokens) with:
               gas gas_remaining wei
              args caller, this.address, _param1
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0]
          if _param1 <= 0:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          34,
                          0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                          Mask(240, 0, _param2)
          require ext_code.size(stakingContractAddress)
          call stakingContractAddress.stake(uint256 stakeAmount) with:
               gas gas_remaining wei
              args _param1
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if not totalSupply:
              if _param1 + totalSupply < totalSupply:
                  revert with 0, 'SafeMath: addition overflow'
              totalSupply += _param1
              if _param1 + balanceOf[caller] < balanceOf[caller]:
                  revert with 0, 'SafeMath: addition overflow'
              balanceOf[caller] += _param1
              log Transfer(
                    address from=_param1,
                    address to=0,
                    uint256 tokens=caller)
          else:
              if totalDeposits * totalSupply / totalSupply != totalDeposits:
                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                              32,
                              33,
                              0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                              Mask(248, 0, _param2)
              if not totalDeposits * totalSupply:
                  if _param1 + totalSupply < totalSupply:
                      revert with 0, 'SafeMath: addition overflow'
                  totalSupply += _param1
                  if _param1 + balanceOf[caller] < balanceOf[caller]:
                      revert with 0, 'SafeMath: addition overflow'
                  balanceOf[caller] += _param1
                  log Transfer(
                        address from=_param1,
                        address to=0,
                        uint256 tokens=caller)
              else:
                  if not _param1:
                      if not totalDeposits:
                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      if (0 / totalDeposits) + totalSupply < totalSupply:
                          revert with 0, 'SafeMath: addition overflow'
                      totalSupply += 0 / totalDeposits
                      if (0 / totalDeposits) + balanceOf[caller] < balanceOf[caller]:
                          revert with 0, 'SafeMath: addition overflow'
                      balanceOf[caller] += 0 / totalDeposits
                      log Transfer(
                            address from=(0 / totalDeposits),
                            address to=0,
                            uint256 tokens=caller)
                  else:
                      if totalSupply * _param1 / _param1 != totalSupply:
                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                      32,
                                      33,
                                      0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                      Mask(248, 0, _param2)
                      if not totalDeposits:
                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      if (totalSupply * _param1 / totalDeposits) + totalSupply < totalSupply:
                          revert with 0, 'SafeMath: addition overflow'
                      totalSupply += totalSupply * _param1 / totalDeposits
                      if (totalSupply * _param1 / totalDeposits) + balanceOf[caller] < balanceOf[caller]:
                          revert with 0, 'SafeMath: addition overflow'
                      balanceOf[caller] += totalSupply * _param1 / totalDeposits
                      log Transfer(
                            address from=(totalSupply * _param1 / totalDeposits),
                            address to=0,
                            uint256 tokens=caller)
          if _param1 + totalDeposits < totalDeposits:
              revert with 0, 'SafeMath: addition overflow'
          totalDeposits += _param1
          log Deposit(
                address sender=_param1,
                uint256 value=caller)
          stop
      require ext_code.size(stakingContractAddress)
      static call stakingContractAddress.0x8cc262 with:
              gas gas_remaining wei
             args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data <= unknown789139bc:
          require ext_code.size(unknownc89039c5Address)
          call unknownc89039c5Address.transferFrom(address from, address to, uint256 tokens) with:
               gas gas_remaining wei
              args caller, this.address, _param1
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0]
          if _param1 <= 0:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          34,
                          0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                          Mask(240, 0, _param2)
          require ext_code.size(stakingContractAddress)
          call stakingContractAddress.stake(uint256 stakeAmount) with:
               gas gas_remaining wei
              args _param1
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if not totalSupply:
              if _param1 + totalSupply < totalSupply:
                  revert with 0, 'SafeMath: addition overflow'
              totalSupply += _param1
              if _param1 + balanceOf[caller] < balanceOf[caller]:
                  revert with 0, 'SafeMath: addition overflow'
              balanceOf[caller] += _param1
              log Transfer(
                    address from=_param1,
                    address to=0,
                    uint256 tokens=caller)
          else:
              if totalDeposits * totalSupply / totalSupply != totalDeposits:
                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                              32,
                              33,
                              0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                              Mask(248, 0, _param2)
              if not totalDeposits * totalSupply:
                  if _param1 + totalSupply < totalSupply:
                      revert with 0, 'SafeMath: addition overflow'
                  totalSupply += _param1
                  if _param1 + balanceOf[caller] < balanceOf[caller]:
                      revert with 0, 'SafeMath: addition overflow'
                  balanceOf[caller] += _param1
                  log Transfer(
                        address from=_param1,
                        address to=0,
                        uint256 tokens=caller)
              else:
                  if not _param1:
                      if not totalDeposits:
                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      if (0 / totalDeposits) + totalSupply < totalSupply:
                          revert with 0, 'SafeMath: addition overflow'
                      totalSupply += 0 / totalDeposits
                      if (0 / totalDeposits) + balanceOf[caller] < balanceOf[caller]:
                          revert with 0, 'SafeMath: addition overflow'
                      balanceOf[caller] += 0 / totalDeposits
                      log Transfer(
                            address from=(0 / totalDeposits),
                            address to=0,
                            uint256 tokens=caller)
                  else:
                      if totalSupply * _param1 / _param1 != totalSupply:
                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                      32,
                                      33,
                                      0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                      Mask(248, 0, _param2)
                      if not totalDeposits:
                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      if (totalSupply * _param1 / totalDeposits) + totalSupply < totalSupply:
                          revert with 0, 'SafeMath: addition overflow'
                      totalSupply += totalSupply * _param1 / totalDeposits
                      if (totalSupply * _param1 / totalDeposits) + balanceOf[caller] < balanceOf[caller]:
                          revert with 0, 'SafeMath: addition overflow'
                      balanceOf[caller] += totalSupply * _param1 / totalDeposits
                      log Transfer(
                            address from=(totalSupply * _param1 / totalDeposits),
                            address to=0,
                            uint256 tokens=caller)
          if _param1 + totalDeposits < totalDeposits:
              revert with 0, 'SafeMath: addition overflow'
          totalDeposits += _param1
          log Deposit(
                address sender=_param1,
                uint256 value=caller)
          stop
      require ext_code.size(stakingContractAddress)
      call stakingContractAddress.getReward() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      if not ext_call.return_data[0]:
          if not ext_call.return_data[0]:
              if not ext_call.return_data[0]:
                  if 0 <= ext_call.return_data[0]:
                      if ext_call.return_data / 2 <= 0:
                          revert with 0, 
                                      32,
                                      50,
                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                      mem[662 len 14]
                      require ext_code.size(unknownc89039c5Address)
                      static call unknownc89039c5Address.0xdfe1681 with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mem[608] = ext_call.return_data[12 len 20]
                      if rewardTokenAddress == mem[620 len 20]:
                          require ext_code.size(unknownc89039c5Address)
                          static call unknownc89039c5Address.token1() with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mem[704] = ext_call.return_data[12 len 20]
                          if rewardTokenAddress == mem[716 len 20]:
                              require ext_code.size(unknownf887ea40Address)
                              call unknownf887ea40Address.0xe8e33700 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataaddr(this.address), block.timestamp
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 96
                              if ext_call.return_data <= 0:
                                  revert with 0, 
                                              32,
                                              34,
                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                              Mask(239, 1, ext_call.return_data[0])
                              require ext_code.size(stakingContractAddress)
                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                   gas gas_remaining wei
                                  args ext_call.return_data[64]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              if ext_call.return_datatotalDeposits < totalDeposits:
                                  revert with 0, 'SafeMath: addition overflow'
                              totalDeposits += ext_call.return_data[64]
                              log 0xc7606d21: ext_call.return_data
              else:
                  if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                      revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                  if not unknown8aff733d * ext_call.return_data / 10000:
                      if 0 <= ext_call.return_data[0]:
                          if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                  revert with 0, 
                                              32,
                                              50,
                                              0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                              mem[662 len 14]
                              require ext_code.size(unknownc89039c5Address)
                              static call unknownc89039c5Address.0xdfe1681 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[608] = ext_call.return_data[12 len 20]
                              if rewardTokenAddress == mem[620 len 20]:
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.token1() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[704] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[716 len 20]:
                                      require ext_code.size(unknownf887ea40Address)
                                      call unknownf887ea40Address.0xe8e33700 with:
                                           gas gas_remaining wei
                                          args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 96
                                      if ext_call.return_data <= 0:
                                          revert with 0, 
                                                      32,
                                                      34,
                                                      0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                      Mask(239, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000))
                                      require ext_code.size(stakingContractAddress)
                                      call stakingContractAddress.stake(uint256 stakeAmount) with:
                                           gas gas_remaining wei
                                          args ext_call.return_data[64]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      if ext_call.return_datatotalDeposits < totalDeposits:
                                          revert with 0, 'SafeMath: addition overflow'
                                      totalDeposits += ext_call.return_data[64]
                                      log 0xc7606d21: ext_call.return_data
                  else:
                      require ext_code.size(rewardTokenAddress)
                      call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                           gas gas_remaining wei
                          args caller, unknown8aff733d * ext_call.return_data / 10000
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not ext_call.return_data[0]:
                          revert with 0, 'DexStrategyV4::_reinvest, reward'
                      if 0 <= ext_call.return_data[0]:
                          if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                  revert with 0, 
                                              32,
                                              50,
                                              0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                              mem[662 len 14]
                              require ext_code.size(unknownc89039c5Address)
                              static call unknownc89039c5Address.0xdfe1681 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[608] = ext_call.return_data[12 len 20]
                              if rewardTokenAddress == mem[620 len 20]:
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.token1() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[704] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[716 len 20]:
                                      require ext_code.size(unknownf887ea40Address)
                                      call unknownf887ea40Address.0xe8e33700 with:
                                           gas gas_remaining wei
                                          args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 96
                                      if ext_call.return_data <= 0:
                                          revert with 0, 
                                                      32,
                                                      34,
                                                      0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                      Mask(239, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000))
                                      require ext_code.size(stakingContractAddress)
                                      call stakingContractAddress.stake(uint256 stakeAmount) with:
                                           gas gas_remaining wei
                                          args ext_call.return_data[64]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
          else:
              if unknown07677111 * ext_call.return_data / ext_call.return_dataunknown07677111:
                  revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, Mask(248, 0, _param4)
              if not unknown07677111 * ext_call.return_data / 10000:
                  if not ext_call.return_data[0]:
                      if 0 <= ext_call.return_data[0]:
                          if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                  if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                      revert with 0, 
                                                  32,
                                                  50,
                                                  0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                  mem[662 len 14]
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.0xdfe1681 with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[608] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[620 len 20]:
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.token1() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[704] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[716 len 20]:
                                          require ext_code.size(unknownf887ea40Address)
                                          call unknownf887ea40Address.0xe8e33700 with:
                                               gas gas_remaining wei
                                              args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 96
                                          if ext_call.return_data <= 0:
                                              revert with 0, 
                                                          32,
                                                          34,
                                                          0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                          Mask(239, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000))
                                          require ext_code.size(stakingContractAddress)
                                          call stakingContractAddress.stake(uint256 stakeAmount) with:
                                               gas gas_remaining wei
                                              args ext_call.return_data[64]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          if ext_call.return_datatotalDeposits < totalDeposits:
                                              revert with 0, 'SafeMath: addition overflow'
                                          totalDeposits += ext_call.return_data[64]
                                          log 0xc7606d21: ext_call.return_data
                  else:
                      if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                          revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                      if not unknown8aff733d * ext_call.return_data / 10000:
                          if 0 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              if ext_call.return_datatotalDeposits < totalDeposits:
                                                  revert with 0, 'SafeMath: addition overflow'
                                              totalDeposits += ext_call.return_data[64]
                                              log 0xc7606d21: ext_call.return_data
                      else:
                          require ext_code.size(rewardTokenAddress)
                          call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                               gas gas_remaining wei
                              args caller, unknown8aff733d * ext_call.return_data / 10000
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              revert with 0, 'DexStrategyV4::_reinvest, reward'
                          if 0 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  require ext_code.size(rewardTokenAddress)
                  call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                       gas gas_remaining wei
                      args owner, unknown07677111 * ext_call.return_data / 10000
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if not ext_call.return_data[0]:
                      revert with 0, 'DexStrategyV4::_reinvest, admin'
                  if not ext_call.return_data[0]:
                      if 0 <= ext_call.return_data[0]:
                          if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                  if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                      revert with 0, 
                                                  32,
                                                  50,
                                                  0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                  mem[662 len 14]
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.0xdfe1681 with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[608] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[620 len 20]:
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.token1() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[704] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[716 len 20]:
                                          require ext_code.size(unknownf887ea40Address)
                                          call unknownf887ea40Address.0xe8e33700 with:
                                               gas gas_remaining wei
                                              args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 96
                                          if ext_call.return_data <= 0:
                                              revert with 0, 
                                                          32,
                                                          34,
                                                          0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                          Mask(239, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000))
                                          require ext_code.size(stakingContractAddress)
                                          call stakingContractAddress.stake(uint256 stakeAmount) with:
                                               gas gas_remaining wei
                                              args ext_call.return_data[64]
                  else:
                      if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                          revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                      if not unknown8aff733d * ext_call.return_data / 10000:
                          if 0 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                      else:
                          require ext_code.size(rewardTokenAddress)
                          call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                               gas gas_remaining wei
                              args caller, unknown8aff733d * ext_call.return_data / 10000
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              revert with 0, 'DexStrategyV4::_reinvest, reward'
                          if 0 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
      else:
          if unknown5ea682ea * ext_call.return_data / ext_call.return_dataunknown5ea682ea:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          33,
                          0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                          Mask(248, 0, _param2)
          if not unknown5ea682ea * ext_call.return_data / 10000:
              if not ext_call.return_data[0]:
                  if not ext_call.return_data[0]:
                      if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                          if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                              if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) / 2 <= 0:
                                  revert with 0, 
                                              32,
                                              50,
                                              0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                              mem[662 len 14]
                              require ext_code.size(unknownc89039c5Address)
                              static call unknownc89039c5Address.0xdfe1681 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[608] = ext_call.return_data[12 len 20]
                              if rewardTokenAddress == mem[620 len 20]:
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.token1() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[704] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[716 len 20]:
                                      require ext_code.size(unknownf887ea40Address)
                                      call unknownf887ea40Address.0xe8e33700 with:
                                           gas gas_remaining wei
                                          args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 96
                                      if ext_call.return_data <= 0:
                                          revert with 0, 
                                                      32,
                                                      34,
                                                      0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                      Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000))
                                      require ext_code.size(stakingContractAddress)
                                      call stakingContractAddress.stake(uint256 stakeAmount) with:
                                           gas gas_remaining wei
                                          args ext_call.return_data[64]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      if ext_call.return_datatotalDeposits < totalDeposits:
                                          revert with 0, 'SafeMath: addition overflow'
                                      totalDeposits += ext_call.return_data[64]
                                      log 0xc7606d21: ext_call.return_data
                  else:
                      if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                          revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                      if not unknown8aff733d * ext_call.return_data / 10000:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              if ext_call.return_datatotalDeposits < totalDeposits:
                                                  revert with 0, 'SafeMath: addition overflow'
                                              totalDeposits += ext_call.return_data[64]
                                              log 0xc7606d21: ext_call.return_data
                      else:
                          require ext_code.size(rewardTokenAddress)
                          call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                               gas gas_remaining wei
                              args caller, unknown8aff733d * ext_call.return_data / 10000
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              revert with 0, 'DexStrategyV4::_reinvest, reward'
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  if unknown07677111 * ext_call.return_data / ext_call.return_dataunknown07677111:
                      revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, Mask(248, 0, _param4)
                  if not unknown07677111 * ext_call.return_data / 10000:
                      if not ext_call.return_data[0]:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              if ext_call.return_datatotalDeposits < totalDeposits:
                                                  revert with 0, 'SafeMath: addition overflow'
                                              totalDeposits += ext_call.return_data[64]
                                              log 0xc7606d21: ext_call.return_data
                      else:
                          if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                              revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                          if not unknown8aff733d * ext_call.return_data / 10000:
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >= 96
                                                  if ext_call.return_data <= 0:
                                                      revert with 0, 
                                                                  32,
                                                                  34,
                                                                  0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                                  Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                                  require ext_code.size(stakingContractAddress)
                                                  call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                       gas gas_remaining wei
                                                      args ext_call.return_data[64]
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  if ext_call.return_datatotalDeposits < totalDeposits:
                                                      revert with 0, 'SafeMath: addition overflow'
                          else:
                              require ext_code.size(rewardTokenAddress)
                              call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                                   gas gas_remaining wei
                                  args caller, unknown8aff733d * ext_call.return_data / 10000
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not ext_call.return_data[0]:
                                  revert with 0, 'DexStrategyV4::_reinvest, reward'
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >= 96
                                                  if ext_call.return_data <= 0:
                                                      revert with 0, 
                                                                  32,
                                                                  34,
                                                                  0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                                  Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                                  require ext_code.size(stakingContractAddress)
                                                  call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                       gas gas_remaining wei
                                                      args ext_call.return_data[64]
                  else:
                      require ext_code.size(rewardTokenAddress)
                      call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                           gas gas_remaining wei
                          args owner, unknown07677111 * ext_call.return_data / 10000
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not ext_call.return_data[0]:
                          revert with 0, 'DexStrategyV4::_reinvest, admin'
                      if not ext_call.return_data[0]:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000))
                      else:
                          if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                              revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                          if not unknown8aff733d * ext_call.return_data / 10000:
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >= 96
                          else:
                              require ext_code.size(rewardTokenAddress)
                              call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                                   gas gas_remaining wei
                                  args caller, unknown8aff733d * ext_call.return_data / 10000
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not ext_call.return_data[0]:
                                  revert with 0, 'DexStrategyV4::_reinvest, reward'
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
          else:
              require ext_code.size(rewardTokenAddress)
              call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                   gas gas_remaining wei
                  args devAddr, unknown5ea682ea * ext_call.return_data / 10000
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'DexStrategyV4::_reinvest, dev'
              if not ext_call.return_data[0]:
                  if not ext_call.return_data[0]:
                      if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                          if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                              if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) / 2 <= 0:
                                  revert with 0, 
                                              32,
                                              50,
                                              0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                              mem[662 len 14]
                              require ext_code.size(unknownc89039c5Address)
                              static call unknownc89039c5Address.0xdfe1681 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[608] = ext_call.return_data[12 len 20]
                              if rewardTokenAddress == mem[620 len 20]:
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.token1() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[704] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[716 len 20]:
                                      require ext_code.size(unknownf887ea40Address)
                                      call unknownf887ea40Address.0xe8e33700 with:
                                           gas gas_remaining wei
                                          args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 96
                                      if ext_call.return_data <= 0:
                                          revert with 0, 
                                                      32,
                                                      34,
                                                      0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                      Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000))
                                      require ext_code.size(stakingContractAddress)
                                      call stakingContractAddress.stake(uint256 stakeAmount) with:
                                           gas gas_remaining wei
                                          args ext_call.return_data[64]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                  else:
                      if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                          revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                      if not unknown8aff733d * ext_call.return_data / 10000:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                      else:
                          require ext_code.size(rewardTokenAddress)
                          call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                               gas gas_remaining wei
                              args caller, unknown8aff733d * ext_call.return_data / 10000
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              revert with 0, 'DexStrategyV4::_reinvest, reward'
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
              else:
                  if unknown07677111 * ext_call.return_data / ext_call.return_dataunknown07677111:
                      revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, Mask(248, 0, _param4)
                  if not unknown07677111 * ext_call.return_data / 10000:
                      if not ext_call.return_data[0]:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                      else:
                          if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                              revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                          if not unknown8aff733d * ext_call.return_data / 10000:
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >= 96
                                                  if ext_call.return_data <= 0:
                                                      revert with 0, 
                                                                  32,
                                                                  34,
                                                                  0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                                  Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                                  require ext_code.size(stakingContractAddress)
                                                  call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                       gas gas_remaining wei
                                                      args ext_call.return_data[64]
                          else:
                              require ext_code.size(rewardTokenAddress)
                              call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                                   gas gas_remaining wei
                                  args caller, unknown8aff733d * ext_call.return_data / 10000
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not ext_call.return_data[0]:
                                  revert with 0, 'DexStrategyV4::_reinvest, reward'
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >= 96
                  else:
                      require ext_code.size(rewardTokenAddress)
                      call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                           gas gas_remaining wei
                          args owner, unknown07677111 * ext_call.return_data / 10000
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not ext_call.return_data[0]:
                          revert with 0, 'DexStrategyV4::_reinvest, admin'
                      if not ext_call.return_data[0]:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                      else:
                          if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                              revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                          if not unknown8aff733d * ext_call.return_data / 10000:
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                          else:
                              require ext_code.size(rewardTokenAddress)
                              call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                                   gas gas_remaining wei
                                  args caller, unknown8aff733d * ext_call.return_data / 10000
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not ext_call.return_data[0]:
                                  revert with 0, 'DexStrategyV4::_reinvest, reward'
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
  else:
      if bool(stor8[caller]) != 1:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      32,
                      46,
                      0x735065726d697373696f6e65643a3a6f6e6c79416c6c6f7765644465706f736974732c206e6f7420616c6c6f7765,
                      Mask(144, 0, _param2)
      if bool(unknownb52a321f) != 1:
          revert with 0, 'DexStrategyV4::_deposit'
      if not unknown789139bc:
          require ext_code.size(unknownc89039c5Address)
          call unknownc89039c5Address.transferFrom(address from, address to, uint256 tokens) with:
               gas gas_remaining wei
              args caller, this.address, _param1
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0]
          if _param1 <= 0:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          34,
                          0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                          Mask(240, 0, _param2)
          require ext_code.size(stakingContractAddress)
          call stakingContractAddress.stake(uint256 stakeAmount) with:
               gas gas_remaining wei
              args _param1
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if not totalSupply:
              if _param1 + totalSupply < totalSupply:
                  revert with 0, 'SafeMath: addition overflow'
              totalSupply += _param1
              if _param1 + balanceOf[caller] < balanceOf[caller]:
                  revert with 0, 'SafeMath: addition overflow'
              balanceOf[caller] += _param1
              log Transfer(
                    address from=_param1,
                    address to=0,
                    uint256 tokens=caller)
          else:
              if totalDeposits * totalSupply / totalSupply != totalDeposits:
                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                              32,
                              33,
                              0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                              Mask(248, 0, _param2)
              if not totalDeposits * totalSupply:
                  if _param1 + totalSupply < totalSupply:
                      revert with 0, 'SafeMath: addition overflow'
                  totalSupply += _param1
                  if _param1 + balanceOf[caller] < balanceOf[caller]:
                      revert with 0, 'SafeMath: addition overflow'
                  balanceOf[caller] += _param1
                  log Transfer(
                        address from=_param1,
                        address to=0,
                        uint256 tokens=caller)
              else:
                  if not _param1:
                      if not totalDeposits:
                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      if (0 / totalDeposits) + totalSupply < totalSupply:
                          revert with 0, 'SafeMath: addition overflow'
                      totalSupply += 0 / totalDeposits
                      if (0 / totalDeposits) + balanceOf[caller] < balanceOf[caller]:
                          revert with 0, 'SafeMath: addition overflow'
                      balanceOf[caller] += 0 / totalDeposits
                      log Transfer(
                            address from=(0 / totalDeposits),
                            address to=0,
                            uint256 tokens=caller)
                  else:
                      if totalSupply * _param1 / _param1 != totalSupply:
                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                      32,
                                      33,
                                      0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                      Mask(248, 0, _param2)
                      if not totalDeposits:
                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      if (totalSupply * _param1 / totalDeposits) + totalSupply < totalSupply:
                          revert with 0, 'SafeMath: addition overflow'
                      totalSupply += totalSupply * _param1 / totalDeposits
                      if (totalSupply * _param1 / totalDeposits) + balanceOf[caller] < balanceOf[caller]:
                          revert with 0, 'SafeMath: addition overflow'
                      balanceOf[caller] += totalSupply * _param1 / totalDeposits
                      log Transfer(
                            address from=(totalSupply * _param1 / totalDeposits),
                            address to=0,
                            uint256 tokens=caller)
          if _param1 + totalDeposits < totalDeposits:
              revert with 0, 'SafeMath: addition overflow'
          totalDeposits += _param1
          log Deposit(
                address sender=_param1,
                uint256 value=caller)
          stop
      require ext_code.size(stakingContractAddress)
      static call stakingContractAddress.0x8cc262 with:
              gas gas_remaining wei
             args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data <= unknown789139bc:
          require ext_code.size(unknownc89039c5Address)
          call unknownc89039c5Address.transferFrom(address from, address to, uint256 tokens) with:
               gas gas_remaining wei
              args caller, this.address, _param1
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0]
          if _param1 <= 0:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          34,
                          0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                          Mask(240, 0, _param2)
          require ext_code.size(stakingContractAddress)
          call stakingContractAddress.stake(uint256 stakeAmount) with:
               gas gas_remaining wei
              args _param1
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if not totalSupply:
              if _param1 + totalSupply < totalSupply:
                  revert with 0, 'SafeMath: addition overflow'
              totalSupply += _param1
              if _param1 + balanceOf[caller] < balanceOf[caller]:
                  revert with 0, 'SafeMath: addition overflow'
              balanceOf[caller] += _param1
              log Transfer(
                    address from=_param1,
                    address to=0,
                    uint256 tokens=caller)
          else:
              if totalDeposits * totalSupply / totalSupply != totalDeposits:
                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                              32,
                              33,
                              0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                              Mask(248, 0, _param2)
              if not totalDeposits * totalSupply:
                  if _param1 + totalSupply < totalSupply:
                      revert with 0, 'SafeMath: addition overflow'
                  totalSupply += _param1
                  if _param1 + balanceOf[caller] < balanceOf[caller]:
                      revert with 0, 'SafeMath: addition overflow'
                  balanceOf[caller] += _param1
                  log Transfer(
                        address from=_param1,
                        address to=0,
                        uint256 tokens=caller)
              else:
                  if not _param1:
                      if not totalDeposits:
                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      if (0 / totalDeposits) + totalSupply < totalSupply:
                          revert with 0, 'SafeMath: addition overflow'
                      totalSupply += 0 / totalDeposits
                      if (0 / totalDeposits) + balanceOf[caller] < balanceOf[caller]:
                          revert with 0, 'SafeMath: addition overflow'
                      balanceOf[caller] += 0 / totalDeposits
                      log Transfer(
                            address from=(0 / totalDeposits),
                            address to=0,
                            uint256 tokens=caller)
                  else:
                      if totalSupply * _param1 / _param1 != totalSupply:
                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                      32,
                                      33,
                                      0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                      Mask(248, 0, _param2)
                      if not totalDeposits:
                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      if (totalSupply * _param1 / totalDeposits) + totalSupply < totalSupply:
                          revert with 0, 'SafeMath: addition overflow'
                      totalSupply += totalSupply * _param1 / totalDeposits
                      if (totalSupply * _param1 / totalDeposits) + balanceOf[caller] < balanceOf[caller]:
                          revert with 0, 'SafeMath: addition overflow'
                      balanceOf[caller] += totalSupply * _param1 / totalDeposits
                      log Transfer(
                            address from=(totalSupply * _param1 / totalDeposits),
                            address to=0,
                            uint256 tokens=caller)
          if _param1 + totalDeposits < totalDeposits:
              revert with 0, 'SafeMath: addition overflow'
          totalDeposits += _param1
          log Deposit(
                address sender=_param1,
                uint256 value=caller)
          stop
      require ext_code.size(stakingContractAddress)
      call stakingContractAddress.getReward() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      if not ext_call.return_data[0]:
          if not ext_call.return_data[0]:
              if not ext_call.return_data[0]:
                  if 0 <= ext_call.return_data[0]:
                      if ext_call.return_data / 2 <= 0:
                          revert with 0, 
                                      32,
                                      50,
                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                      mem[662 len 14]
                      require ext_code.size(unknownc89039c5Address)
                      static call unknownc89039c5Address.0xdfe1681 with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mem[608] = ext_call.return_data[12 len 20]
                      if rewardTokenAddress == mem[620 len 20]:
                          require ext_code.size(unknownc89039c5Address)
                          static call unknownc89039c5Address.token1() with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mem[704] = ext_call.return_data[12 len 20]
                          if rewardTokenAddress == mem[716 len 20]:
                              require ext_code.size(unknownf887ea40Address)
                              call unknownf887ea40Address.0xe8e33700 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataaddr(this.address), block.timestamp
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 96
                              if ext_call.return_data <= 0:
                                  revert with 0, 
                                              32,
                                              34,
                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                              Mask(239, 1, ext_call.return_data[0])
                              require ext_code.size(stakingContractAddress)
                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                   gas gas_remaining wei
                                  args ext_call.return_data[64]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              if ext_call.return_datatotalDeposits < totalDeposits:
                                  revert with 0, 'SafeMath: addition overflow'
                              totalDeposits += ext_call.return_data[64]
                              log 0xc7606d21: ext_call.return_data
              else:
                  if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                      revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                  if not unknown8aff733d * ext_call.return_data / 10000:
                      if 0 <= ext_call.return_data[0]:
                          if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                  revert with 0, 
                                              32,
                                              50,
                                              0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                              mem[662 len 14]
                              require ext_code.size(unknownc89039c5Address)
                              static call unknownc89039c5Address.0xdfe1681 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[608] = ext_call.return_data[12 len 20]
                              if rewardTokenAddress == mem[620 len 20]:
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.token1() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[704] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[716 len 20]:
                                      require ext_code.size(unknownf887ea40Address)
                                      call unknownf887ea40Address.0xe8e33700 with:
                                           gas gas_remaining wei
                                          args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 96
                                      if ext_call.return_data <= 0:
                                          revert with 0, 
                                                      32,
                                                      34,
                                                      0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                      Mask(239, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000))
                                      require ext_code.size(stakingContractAddress)
                                      call stakingContractAddress.stake(uint256 stakeAmount) with:
                                           gas gas_remaining wei
                                          args ext_call.return_data[64]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      if ext_call.return_datatotalDeposits < totalDeposits:
                                          revert with 0, 'SafeMath: addition overflow'
                                      totalDeposits += ext_call.return_data[64]
                                      log 0xc7606d21: ext_call.return_data
                  else:
                      require ext_code.size(rewardTokenAddress)
                      call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                           gas gas_remaining wei
                          args caller, unknown8aff733d * ext_call.return_data / 10000
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not ext_call.return_data[0]:
                          revert with 0, 'DexStrategyV4::_reinvest, reward'
                      if 0 <= ext_call.return_data[0]:
                          if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                  revert with 0, 
                                              32,
                                              50,
                                              0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                              mem[662 len 14]
                              require ext_code.size(unknownc89039c5Address)
                              static call unknownc89039c5Address.0xdfe1681 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[608] = ext_call.return_data[12 len 20]
                              if rewardTokenAddress == mem[620 len 20]:
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.token1() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[704] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[716 len 20]:
                                      require ext_code.size(unknownf887ea40Address)
                                      call unknownf887ea40Address.0xe8e33700 with:
                                           gas gas_remaining wei
                                          args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 96
                                      if ext_call.return_data <= 0:
                                          revert with 0, 
                                                      32,
                                                      34,
                                                      0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                      Mask(239, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000))
                                      require ext_code.size(stakingContractAddress)
                                      call stakingContractAddress.stake(uint256 stakeAmount) with:
                                           gas gas_remaining wei
                                          args ext_call.return_data[64]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
          else:
              if unknown07677111 * ext_call.return_data / ext_call.return_dataunknown07677111:
                  revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, Mask(248, 0, _param4)
              if not unknown07677111 * ext_call.return_data / 10000:
                  if not ext_call.return_data[0]:
                      if 0 <= ext_call.return_data[0]:
                          if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                  if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                      revert with 0, 
                                                  32,
                                                  50,
                                                  0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                  mem[662 len 14]
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.0xdfe1681 with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[608] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[620 len 20]:
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.token1() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[704] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[716 len 20]:
                                          require ext_code.size(unknownf887ea40Address)
                                          call unknownf887ea40Address.0xe8e33700 with:
                                               gas gas_remaining wei
                                              args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 96
                                          if ext_call.return_data <= 0:
                                              revert with 0, 
                                                          32,
                                                          34,
                                                          0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                          Mask(239, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000))
                                          require ext_code.size(stakingContractAddress)
                                          call stakingContractAddress.stake(uint256 stakeAmount) with:
                                               gas gas_remaining wei
                                              args ext_call.return_data[64]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          if ext_call.return_datatotalDeposits < totalDeposits:
                                              revert with 0, 'SafeMath: addition overflow'
                                          totalDeposits += ext_call.return_data[64]
                                          log 0xc7606d21: ext_call.return_data
                  else:
                      if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                          revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                      if not unknown8aff733d * ext_call.return_data / 10000:
                          if 0 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              if ext_call.return_datatotalDeposits < totalDeposits:
                                                  revert with 0, 'SafeMath: addition overflow'
                      else:
                          require ext_code.size(rewardTokenAddress)
                          call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                               gas gas_remaining wei
                              args caller, unknown8aff733d * ext_call.return_data / 10000
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              revert with 0, 'DexStrategyV4::_reinvest, reward'
                          if 0 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
              else:
                  require ext_code.size(rewardTokenAddress)
                  call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                       gas gas_remaining wei
                      args owner, unknown07677111 * ext_call.return_data / 10000
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if not ext_call.return_data[0]:
                      revert with 0, 'DexStrategyV4::_reinvest, admin'
                  if not ext_call.return_data[0]:
                      if 0 <= ext_call.return_data[0]:
                          if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                  if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                      revert with 0, 
                                                  32,
                                                  50,
                                                  0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                  mem[662 len 14]
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.0xdfe1681 with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[608] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[620 len 20]:
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.token1() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[704] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[716 len 20]:
                                          require ext_code.size(unknownf887ea40Address)
                                          call unknownf887ea40Address.0xe8e33700 with:
                                               gas gas_remaining wei
                                              args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 96
                                          if ext_call.return_data <= 0:
                                              revert with 0, 
                                                          32,
                                                          34,
                                                          0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                          Mask(239, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000))
                  else:
                      if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                          revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                      if not unknown8aff733d * ext_call.return_data / 10000:
                          if 0 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                      else:
                          require ext_code.size(rewardTokenAddress)
                          call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                               gas gas_remaining wei
                              args caller, unknown8aff733d * ext_call.return_data / 10000
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              revert with 0, 'DexStrategyV4::_reinvest, reward'
                          if 0 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
      else:
          if unknown5ea682ea * ext_call.return_data / ext_call.return_dataunknown5ea682ea:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          33,
                          0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                          Mask(248, 0, _param2)
          if not unknown5ea682ea * ext_call.return_data / 10000:
              if ext_call.return_data[0]:
                  if unknown07677111 * ext_call.return_data / ext_call.return_dataunknown07677111:
                      revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, Mask(248, 0, _param4)
                  if not unknown07677111 * ext_call.return_data / 10000:
                      if not ext_call.return_data[0]:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              if ext_call.return_datatotalDeposits < totalDeposits:
                                                  revert with 0, 'SafeMath: addition overflow'
                      else:
                          if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                              revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                          if not unknown8aff733d * ext_call.return_data / 10000:
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >= 96
                                                  if ext_call.return_data <= 0:
                                                      revert with 0, 
                                                                  32,
                                                                  34,
                                                                  0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                                  Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                                  require ext_code.size(stakingContractAddress)
                                                  call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                       gas gas_remaining wei
                                                      args ext_call.return_data[64]
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require ext_code.size(rewardTokenAddress)
                              call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                                   gas gas_remaining wei
                                  args caller, unknown8aff733d * ext_call.return_data / 10000
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not ext_call.return_data[0]:
                                  revert with 0, 'DexStrategyV4::_reinvest, reward'
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >= 96
                                                  if ext_call.return_data <= 0:
                                                      revert with 0, 
                                                                  32,
                                                                  34,
                                                                  0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                                  Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                  else:
                      require ext_code.size(rewardTokenAddress)
                      call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                           gas gas_remaining wei
                          args owner, unknown07677111 * ext_call.return_data / 10000
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not ext_call.return_data[0]:
                          revert with 0, 'DexStrategyV4::_reinvest, admin'
                      if not ext_call.return_data[0]:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                      else:
                          if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                              revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                          if not unknown8aff733d * ext_call.return_data / 10000:
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >= 96
                          else:
                              require ext_code.size(rewardTokenAddress)
                              call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                                   gas gas_remaining wei
                                  args caller, unknown8aff733d * ext_call.return_data / 10000
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not ext_call.return_data[0]:
                                  revert with 0, 'DexStrategyV4::_reinvest, reward'
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
              else:
                  if not ext_call.return_data[0]:
                      if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                          if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                              if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) / 2 <= 0:
                                  revert with 0, 
                                              32,
                                              50,
                                              0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                              mem[662 len 14]
                              require ext_code.size(unknownc89039c5Address)
                              static call unknownc89039c5Address.0xdfe1681 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[608] = ext_call.return_data[12 len 20]
                              if rewardTokenAddress == mem[620 len 20]:
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.token1() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[704] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[716 len 20]:
                                      require ext_code.size(unknownf887ea40Address)
                                      call unknownf887ea40Address.0xe8e33700 with:
                                           gas gas_remaining wei
                                          args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 96
                                      if ext_call.return_data <= 0:
                                          revert with 0, 
                                                      32,
                                                      34,
                                                      0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                      Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000))
                                      require ext_code.size(stakingContractAddress)
                                      call stakingContractAddress.stake(uint256 stakeAmount) with:
                                           gas gas_remaining wei
                                          args ext_call.return_data[64]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      if ext_call.return_datatotalDeposits < totalDeposits:
                                          revert with 0, 'SafeMath: addition overflow'
                                      totalDeposits += ext_call.return_data[64]
                                      log 0xc7606d21: ext_call.return_data
                  else:
                      if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                          revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                      if not unknown8aff733d * ext_call.return_data / 10000:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              if ext_call.return_datatotalDeposits < totalDeposits:
                                                  revert with 0, 'SafeMath: addition overflow'
                      else:
                          require ext_code.size(rewardTokenAddress)
                          call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                               gas gas_remaining wei
                              args caller, unknown8aff733d * ext_call.return_data / 10000
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              revert with 0, 'DexStrategyV4::_reinvest, reward'
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
          else:
              require ext_code.size(rewardTokenAddress)
              call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                   gas gas_remaining wei
                  args devAddr, unknown5ea682ea * ext_call.return_data / 10000
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'DexStrategyV4::_reinvest, dev'
              if not ext_call.return_data[0]:
                  if not ext_call.return_data[0]:
                      if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                          if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                              if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) / 2 <= 0:
                                  revert with 0, 
                                              32,
                                              50,
                                              0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                              mem[662 len 14]
                              require ext_code.size(unknownc89039c5Address)
                              static call unknownc89039c5Address.0xdfe1681 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[608] = ext_call.return_data[12 len 20]
                              if rewardTokenAddress == mem[620 len 20]:
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.token1() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[704] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[716 len 20]:
                                      require ext_code.size(unknownf887ea40Address)
                                      call unknownf887ea40Address.0xe8e33700 with:
                                           gas gas_remaining wei
                                          args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 96
                                      if ext_call.return_data <= 0:
                                          revert with 0, 
                                                      32,
                                                      34,
                                                      0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                      Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000))
                                      require ext_code.size(stakingContractAddress)
                                      call stakingContractAddress.stake(uint256 stakeAmount) with:
                                           gas gas_remaining wei
                                          args ext_call.return_data[64]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                  else:
                      if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                          revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                      if not unknown8aff733d * ext_call.return_data / 10000:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                      else:
                          require ext_code.size(rewardTokenAddress)
                          call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                               gas gas_remaining wei
                              args caller, unknown8aff733d * ext_call.return_data / 10000
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              revert with 0, 'DexStrategyV4::_reinvest, reward'
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
              else:
                  if unknown07677111 * ext_call.return_data / ext_call.return_dataunknown07677111:
                      revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, Mask(248, 0, _param4)
                  if unknown07677111 * ext_call.return_data / 10000:
                      require ext_code.size(rewardTokenAddress)
                      call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                           gas gas_remaining wei
                          args owner, unknown07677111 * ext_call.return_data / 10000
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not ext_call.return_data[0]:
                          revert with 0, 'DexStrategyV4::_reinvest, admin'
                      if not ext_call.return_data[0]:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                      else:
                          if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                              revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                          if not unknown8aff733d * ext_call.return_data / 10000:
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                          else:
                              require ext_code.size(rewardTokenAddress)
                              call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                                   gas gas_remaining wei
                                  args caller, unknown8aff733d * ext_call.return_data / 10000
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not ext_call.return_data[0]:
                                  revert with 0, 'DexStrategyV4::_reinvest, reward'
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                  else:
                      if not ext_call.return_data[0]:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                      else:
                          if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                              revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                          if not unknown8aff733d * ext_call.return_data / 10000:
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >= 96
                                                  if ext_call.return_data <= 0:
                                                      revert with 0, 
                                                                  32,
                                                                  34,
                                                                  0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                                  Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                          else:
                              require ext_code.size(rewardTokenAddress)
                              call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                                   gas gas_remaining wei
                                  args caller, unknown8aff733d * ext_call.return_data / 10000
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not ext_call.return_data[0]:
                                  revert with 0, 'DexStrategyV4::_reinvest, reward'
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)

def unknown2f4f21e2(addr _param1, uint256 _param2) payable: 
  require calldata.size - 4 >= 64
  if not unknown3bdc6e72:
      if bool(unknownb52a321f) != 1:
          revert with 0, 'DexStrategyV4::_deposit'
      if not unknown789139bc:
          require ext_code.size(unknownc89039c5Address)
          call unknownc89039c5Address.transferFrom(address from, address to, uint256 tokens) with:
               gas gas_remaining wei
              args caller, this.address, _param2
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0]
          if _param2 <= 0:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          34,
                          0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                          mem[198 len 30]
          require ext_code.size(stakingContractAddress)
          call stakingContractAddress.stake(uint256 stakeAmount) with:
               gas gas_remaining wei
              args _param2
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if not totalSupply:
              if _param2 + totalSupply < totalSupply:
                  revert with 0, 'SafeMath: addition overflow'
              totalSupply += _param2
              if _param2 + balanceOf[addr(_param1)] < balanceOf[addr(_param1)]:
                  revert with 0, 'SafeMath: addition overflow'
              balanceOf[addr(_param1)] += _param2
              log Transfer(
                    address from=_param2,
                    address to=0,
                    uint256 tokens=_param1)
          else:
              if totalDeposits * totalSupply / totalSupply != totalDeposits:
                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                              32,
                              33,
                              0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                              mem[197 len 31]
              if not totalDeposits * totalSupply:
                  if _param2 + totalSupply < totalSupply:
                      revert with 0, 'SafeMath: addition overflow'
                  totalSupply += _param2
                  if _param2 + balanceOf[addr(_param1)] < balanceOf[addr(_param1)]:
                      revert with 0, 'SafeMath: addition overflow'
                  balanceOf[addr(_param1)] += _param2
                  log Transfer(
                        address from=_param2,
                        address to=0,
                        uint256 tokens=_param1)
              else:
                  if not _param2:
                      if not totalDeposits:
                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      if (0 / totalDeposits) + totalSupply < totalSupply:
                          revert with 0, 'SafeMath: addition overflow'
                      totalSupply += 0 / totalDeposits
                      if (0 / totalDeposits) + balanceOf[addr(_param1)] < balanceOf[addr(_param1)]:
                          revert with 0, 'SafeMath: addition overflow'
                      balanceOf[addr(_param1)] += 0 / totalDeposits
                      log Transfer(
                            address from=(0 / totalDeposits),
                            address to=0,
                            uint256 tokens=_param1)
                  else:
                      if totalSupply * _param2 / _param2 != totalSupply:
                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                      32,
                                      33,
                                      0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                      mem[197 len 31]
                      if not totalDeposits:
                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      if (totalSupply * _param2 / totalDeposits) + totalSupply < totalSupply:
                          revert with 0, 'SafeMath: addition overflow'
                      totalSupply += totalSupply * _param2 / totalDeposits
                      if (totalSupply * _param2 / totalDeposits) + balanceOf[addr(_param1)] < balanceOf[addr(_param1)]:
                          revert with 0, 'SafeMath: addition overflow'
                      balanceOf[addr(_param1)] += totalSupply * _param2 / totalDeposits
                      log Transfer(
                            address from=(totalSupply * _param2 / totalDeposits),
                            address to=0,
                            uint256 tokens=_param1)
          if _param2 + totalDeposits < totalDeposits:
              revert with 0, 'SafeMath: addition overflow'
          totalDeposits += _param2
          log Deposit(
                address sender=_param2,
                uint256 value=_param1)
          stop
      require ext_code.size(stakingContractAddress)
      static call stakingContractAddress.0x8cc262 with:
              gas gas_remaining wei
             args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data <= unknown789139bc:
          require ext_code.size(unknownc89039c5Address)
          call unknownc89039c5Address.transferFrom(address from, address to, uint256 tokens) with:
               gas gas_remaining wei
              args caller, this.address, _param2
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0]
          if _param2 <= 0:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          34,
                          0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                          mem[198 len 30]
          require ext_code.size(stakingContractAddress)
          call stakingContractAddress.stake(uint256 stakeAmount) with:
               gas gas_remaining wei
              args _param2
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if not totalSupply:
              if _param2 + totalSupply < totalSupply:
                  revert with 0, 'SafeMath: addition overflow'
              totalSupply += _param2
              if _param2 + balanceOf[addr(_param1)] < balanceOf[addr(_param1)]:
                  revert with 0, 'SafeMath: addition overflow'
              balanceOf[addr(_param1)] += _param2
              log Transfer(
                    address from=_param2,
                    address to=0,
                    uint256 tokens=_param1)
          else:
              if totalDeposits * totalSupply / totalSupply != totalDeposits:
                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                              32,
                              33,
                              0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                              mem[197 len 31]
              if not totalDeposits * totalSupply:
                  if _param2 + totalSupply < totalSupply:
                      revert with 0, 'SafeMath: addition overflow'
                  totalSupply += _param2
                  if _param2 + balanceOf[addr(_param1)] < balanceOf[addr(_param1)]:
                      revert with 0, 'SafeMath: addition overflow'
                  balanceOf[addr(_param1)] += _param2
                  log Transfer(
                        address from=_param2,
                        address to=0,
                        uint256 tokens=_param1)
              else:
                  if not _param2:
                      if not totalDeposits:
                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      if (0 / totalDeposits) + totalSupply < totalSupply:
                          revert with 0, 'SafeMath: addition overflow'
                      totalSupply += 0 / totalDeposits
                      if (0 / totalDeposits) + balanceOf[addr(_param1)] < balanceOf[addr(_param1)]:
                          revert with 0, 'SafeMath: addition overflow'
                      balanceOf[addr(_param1)] += 0 / totalDeposits
                      log Transfer(
                            address from=(0 / totalDeposits),
                            address to=0,
                            uint256 tokens=_param1)
                  else:
                      if totalSupply * _param2 / _param2 != totalSupply:
                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                      32,
                                      33,
                                      0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                      mem[197 len 31]
                      if not totalDeposits:
                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      if (totalSupply * _param2 / totalDeposits) + totalSupply < totalSupply:
                          revert with 0, 'SafeMath: addition overflow'
                      totalSupply += totalSupply * _param2 / totalDeposits
                      if (totalSupply * _param2 / totalDeposits) + balanceOf[addr(_param1)] < balanceOf[addr(_param1)]:
                          revert with 0, 'SafeMath: addition overflow'
                      balanceOf[addr(_param1)] += totalSupply * _param2 / totalDeposits
                      log Transfer(
                            address from=(totalSupply * _param2 / totalDeposits),
                            address to=0,
                            uint256 tokens=_param1)
          if _param2 + totalDeposits < totalDeposits:
              revert with 0, 'SafeMath: addition overflow'
          totalDeposits += _param2
          log Deposit(
                address sender=_param2,
                uint256 value=_param1)
          stop
      require ext_code.size(stakingContractAddress)
      call stakingContractAddress.getReward() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      if not ext_call.return_data[0]:
          if not ext_call.return_data[0]:
              if not ext_call.return_data[0]:
                  if 0 <= ext_call.return_data[0]:
                      if ext_call.return_data / 2 <= 0:
                          revert with 0, 
                                      32,
                                      50,
                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                      mem[662 len 14]
                      require ext_code.size(unknownc89039c5Address)
                      static call unknownc89039c5Address.0xdfe1681 with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mem[608] = ext_call.return_data[12 len 20]
                      if rewardTokenAddress == mem[620 len 20]:
                          require ext_code.size(unknownc89039c5Address)
                          static call unknownc89039c5Address.token1() with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mem[704] = ext_call.return_data[12 len 20]
                          if rewardTokenAddress == mem[716 len 20]:
                              require ext_code.size(unknownf887ea40Address)
                              call unknownf887ea40Address.0xe8e33700 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataaddr(this.address), block.timestamp
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 96
                              if ext_call.return_data <= 0:
                                  revert with 0, 
                                              32,
                                              34,
                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                              Mask(239, 1, ext_call.return_data[0])
                              require ext_code.size(stakingContractAddress)
                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                   gas gas_remaining wei
                                  args ext_call.return_data[64]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              if ext_call.return_datatotalDeposits < totalDeposits:
                                  revert with 0, 'SafeMath: addition overflow'
                              totalDeposits += ext_call.return_data[64]
                              log 0xc7606d21: ext_call.return_data
              else:
                  if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                      revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                  if not unknown8aff733d * ext_call.return_data / 10000:
                      if 0 <= ext_call.return_data[0]:
                          if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                  revert with 0, 
                                              32,
                                              50,
                                              0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                              mem[662 len 14]
                              require ext_code.size(unknownc89039c5Address)
                              static call unknownc89039c5Address.0xdfe1681 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[608] = ext_call.return_data[12 len 20]
                              if rewardTokenAddress == mem[620 len 20]:
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.token1() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[704] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[716 len 20]:
                                      require ext_code.size(unknownf887ea40Address)
                                      call unknownf887ea40Address.0xe8e33700 with:
                                           gas gas_remaining wei
                                          args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 96
                                      if ext_call.return_data <= 0:
                                          revert with 0, 
                                                      32,
                                                      34,
                                                      0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                      Mask(239, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000))
                                      require ext_code.size(stakingContractAddress)
                                      call stakingContractAddress.stake(uint256 stakeAmount) with:
                                           gas gas_remaining wei
                                          args ext_call.return_data[64]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      if ext_call.return_datatotalDeposits < totalDeposits:
                                          revert with 0, 'SafeMath: addition overflow'
                                      totalDeposits += ext_call.return_data[64]
                                      log 0xc7606d21: ext_call.return_data
                  else:
                      require ext_code.size(rewardTokenAddress)
                      call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                           gas gas_remaining wei
                          args caller, unknown8aff733d * ext_call.return_data / 10000
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not ext_call.return_data[0]:
                          revert with 0, 'DexStrategyV4::_reinvest, reward'
                      if 0 <= ext_call.return_data[0]:
                          if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                  revert with 0, 
                                              32,
                                              50,
                                              0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                              mem[662 len 14]
                              require ext_code.size(unknownc89039c5Address)
                              static call unknownc89039c5Address.0xdfe1681 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[608] = ext_call.return_data[12 len 20]
                              if rewardTokenAddress == mem[620 len 20]:
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.token1() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[704] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[716 len 20]:
                                      require ext_code.size(unknownf887ea40Address)
                                      call unknownf887ea40Address.0xe8e33700 with:
                                           gas gas_remaining wei
                                          args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 96
                                      if ext_call.return_data <= 0:
                                          revert with 0, 
                                                      32,
                                                      34,
                                                      0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                      Mask(239, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000))
                                      require ext_code.size(stakingContractAddress)
                                      call stakingContractAddress.stake(uint256 stakeAmount) with:
                                           gas gas_remaining wei
                                          args ext_call.return_data[64]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
          else:
              if unknown07677111 * ext_call.return_data / ext_call.return_dataunknown07677111:
                  revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[261 len 31]
              if not unknown07677111 * ext_call.return_data / 10000:
                  if not ext_call.return_data[0]:
                      if 0 <= ext_call.return_data[0]:
                          if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                  if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                      revert with 0, 
                                                  32,
                                                  50,
                                                  0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                  mem[662 len 14]
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.0xdfe1681 with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[608] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[620 len 20]:
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.token1() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[704] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[716 len 20]:
                                          require ext_code.size(unknownf887ea40Address)
                                          call unknownf887ea40Address.0xe8e33700 with:
                                               gas gas_remaining wei
                                              args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 96
                                          if ext_call.return_data <= 0:
                                              revert with 0, 
                                                          32,
                                                          34,
                                                          0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                          Mask(239, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000))
                                          require ext_code.size(stakingContractAddress)
                                          call stakingContractAddress.stake(uint256 stakeAmount) with:
                                               gas gas_remaining wei
                                              args ext_call.return_data[64]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          if ext_call.return_datatotalDeposits < totalDeposits:
                                              revert with 0, 'SafeMath: addition overflow'
                                          totalDeposits += ext_call.return_data[64]
                                          log 0xc7606d21: ext_call.return_data
                  else:
                      if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                          revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                      if not unknown8aff733d * ext_call.return_data / 10000:
                          if 0 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              if ext_call.return_datatotalDeposits < totalDeposits:
                                                  revert with 0, 'SafeMath: addition overflow'
                                              totalDeposits += ext_call.return_data[64]
                                              log 0xc7606d21: ext_call.return_data
                      else:
                          require ext_code.size(rewardTokenAddress)
                          call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                               gas gas_remaining wei
                              args caller, unknown8aff733d * ext_call.return_data / 10000
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              revert with 0, 'DexStrategyV4::_reinvest, reward'
                          if 0 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  require ext_code.size(rewardTokenAddress)
                  call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                       gas gas_remaining wei
                      args owner, unknown07677111 * ext_call.return_data / 10000
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if not ext_call.return_data[0]:
                      revert with 0, 'DexStrategyV4::_reinvest, admin'
                  if not ext_call.return_data[0]:
                      if 0 <= ext_call.return_data[0]:
                          if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                  if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                      revert with 0, 
                                                  32,
                                                  50,
                                                  0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                  mem[662 len 14]
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.0xdfe1681 with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[608] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[620 len 20]:
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.token1() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[704] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[716 len 20]:
                                          require ext_code.size(unknownf887ea40Address)
                                          call unknownf887ea40Address.0xe8e33700 with:
                                               gas gas_remaining wei
                                              args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 96
                                          if ext_call.return_data <= 0:
                                              revert with 0, 
                                                          32,
                                                          34,
                                                          0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                          Mask(239, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000))
                                          require ext_code.size(stakingContractAddress)
                                          call stakingContractAddress.stake(uint256 stakeAmount) with:
                                               gas gas_remaining wei
                                              args ext_call.return_data[64]
                  else:
                      if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                          revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                      if not unknown8aff733d * ext_call.return_data / 10000:
                          if 0 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                      else:
                          require ext_code.size(rewardTokenAddress)
                          call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                               gas gas_remaining wei
                              args caller, unknown8aff733d * ext_call.return_data / 10000
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              revert with 0, 'DexStrategyV4::_reinvest, reward'
                          if 0 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
      else:
          if unknown5ea682ea * ext_call.return_data / ext_call.return_dataunknown5ea682ea:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          33,
                          0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                          mem[197 len 31]
          if not unknown5ea682ea * ext_call.return_data / 10000:
              if not ext_call.return_data[0]:
                  if not ext_call.return_data[0]:
                      if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                          if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                              if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) / 2 <= 0:
                                  revert with 0, 
                                              32,
                                              50,
                                              0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                              mem[662 len 14]
                              require ext_code.size(unknownc89039c5Address)
                              static call unknownc89039c5Address.0xdfe1681 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[608] = ext_call.return_data[12 len 20]
                              if rewardTokenAddress == mem[620 len 20]:
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.token1() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[704] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[716 len 20]:
                                      require ext_code.size(unknownf887ea40Address)
                                      call unknownf887ea40Address.0xe8e33700 with:
                                           gas gas_remaining wei
                                          args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 96
                                      if ext_call.return_data <= 0:
                                          revert with 0, 
                                                      32,
                                                      34,
                                                      0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                      Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000))
                                      require ext_code.size(stakingContractAddress)
                                      call stakingContractAddress.stake(uint256 stakeAmount) with:
                                           gas gas_remaining wei
                                          args ext_call.return_data[64]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      if ext_call.return_datatotalDeposits < totalDeposits:
                                          revert with 0, 'SafeMath: addition overflow'
                                      totalDeposits += ext_call.return_data[64]
                                      log 0xc7606d21: ext_call.return_data
                  else:
                      if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                          revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                      if not unknown8aff733d * ext_call.return_data / 10000:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              if ext_call.return_datatotalDeposits < totalDeposits:
                                                  revert with 0, 'SafeMath: addition overflow'
                                              totalDeposits += ext_call.return_data[64]
                                              log 0xc7606d21: ext_call.return_data
                      else:
                          require ext_code.size(rewardTokenAddress)
                          call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                               gas gas_remaining wei
                              args caller, unknown8aff733d * ext_call.return_data / 10000
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              revert with 0, 'DexStrategyV4::_reinvest, reward'
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  if unknown07677111 * ext_call.return_data / ext_call.return_dataunknown07677111:
                      revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[261 len 31]
                  if not unknown07677111 * ext_call.return_data / 10000:
                      if not ext_call.return_data[0]:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              if ext_call.return_datatotalDeposits < totalDeposits:
                                                  revert with 0, 'SafeMath: addition overflow'
                                              totalDeposits += ext_call.return_data[64]
                                              log 0xc7606d21: ext_call.return_data
                      else:
                          if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                              revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                          if not unknown8aff733d * ext_call.return_data / 10000:
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >= 96
                                                  if ext_call.return_data <= 0:
                                                      revert with 0, 
                                                                  32,
                                                                  34,
                                                                  0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                                  Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                                  require ext_code.size(stakingContractAddress)
                                                  call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                       gas gas_remaining wei
                                                      args ext_call.return_data[64]
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  if ext_call.return_datatotalDeposits < totalDeposits:
                                                      revert with 0, 'SafeMath: addition overflow'
                          else:
                              require ext_code.size(rewardTokenAddress)
                              call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                                   gas gas_remaining wei
                                  args caller, unknown8aff733d * ext_call.return_data / 10000
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not ext_call.return_data[0]:
                                  revert with 0, 'DexStrategyV4::_reinvest, reward'
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >= 96
                                                  if ext_call.return_data <= 0:
                                                      revert with 0, 
                                                                  32,
                                                                  34,
                                                                  0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                                  Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                                  require ext_code.size(stakingContractAddress)
                                                  call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                       gas gas_remaining wei
                                                      args ext_call.return_data[64]
                  else:
                      require ext_code.size(rewardTokenAddress)
                      call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                           gas gas_remaining wei
                          args owner, unknown07677111 * ext_call.return_data / 10000
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not ext_call.return_data[0]:
                          revert with 0, 'DexStrategyV4::_reinvest, admin'
                      if not ext_call.return_data[0]:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000))
                      else:
                          if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                              revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                          if not unknown8aff733d * ext_call.return_data / 10000:
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >= 96
                          else:
                              require ext_code.size(rewardTokenAddress)
                              call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                                   gas gas_remaining wei
                                  args caller, unknown8aff733d * ext_call.return_data / 10000
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not ext_call.return_data[0]:
                                  revert with 0, 'DexStrategyV4::_reinvest, reward'
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
          else:
              require ext_code.size(rewardTokenAddress)
              call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                   gas gas_remaining wei
                  args devAddr, unknown5ea682ea * ext_call.return_data / 10000
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'DexStrategyV4::_reinvest, dev'
              if not ext_call.return_data[0]:
                  if not ext_call.return_data[0]:
                      if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                          if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                              if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) / 2 <= 0:
                                  revert with 0, 
                                              32,
                                              50,
                                              0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                              mem[662 len 14]
                              require ext_code.size(unknownc89039c5Address)
                              static call unknownc89039c5Address.0xdfe1681 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[608] = ext_call.return_data[12 len 20]
                              if rewardTokenAddress == mem[620 len 20]:
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.token1() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[704] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[716 len 20]:
                                      require ext_code.size(unknownf887ea40Address)
                                      call unknownf887ea40Address.0xe8e33700 with:
                                           gas gas_remaining wei
                                          args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 96
                                      if ext_call.return_data <= 0:
                                          revert with 0, 
                                                      32,
                                                      34,
                                                      0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                      Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000))
                                      require ext_code.size(stakingContractAddress)
                                      call stakingContractAddress.stake(uint256 stakeAmount) with:
                                           gas gas_remaining wei
                                          args ext_call.return_data[64]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                  else:
                      if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                          revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                      if not unknown8aff733d * ext_call.return_data / 10000:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                      else:
                          require ext_code.size(rewardTokenAddress)
                          call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                               gas gas_remaining wei
                              args caller, unknown8aff733d * ext_call.return_data / 10000
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              revert with 0, 'DexStrategyV4::_reinvest, reward'
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
              else:
                  if unknown07677111 * ext_call.return_data / ext_call.return_dataunknown07677111:
                      revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[261 len 31]
                  if not unknown07677111 * ext_call.return_data / 10000:
                      if not ext_call.return_data[0]:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                      else:
                          if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                              revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                          if not unknown8aff733d * ext_call.return_data / 10000:
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >= 96
                                                  if ext_call.return_data <= 0:
                                                      revert with 0, 
                                                                  32,
                                                                  34,
                                                                  0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                                  Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                                  require ext_code.size(stakingContractAddress)
                                                  call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                       gas gas_remaining wei
                                                      args ext_call.return_data[64]
                          else:
                              require ext_code.size(rewardTokenAddress)
                              call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                                   gas gas_remaining wei
                                  args caller, unknown8aff733d * ext_call.return_data / 10000
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not ext_call.return_data[0]:
                                  revert with 0, 'DexStrategyV4::_reinvest, reward'
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >= 96
                  else:
                      require ext_code.size(rewardTokenAddress)
                      call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                           gas gas_remaining wei
                          args owner, unknown07677111 * ext_call.return_data / 10000
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not ext_call.return_data[0]:
                          revert with 0, 'DexStrategyV4::_reinvest, admin'
                      if not ext_call.return_data[0]:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                      else:
                          if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                              revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                          if not unknown8aff733d * ext_call.return_data / 10000:
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                          else:
                              require ext_code.size(rewardTokenAddress)
                              call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                                   gas gas_remaining wei
                                  args caller, unknown8aff733d * ext_call.return_data / 10000
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not ext_call.return_data[0]:
                                  revert with 0, 'DexStrategyV4::_reinvest, reward'
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
  else:
      if bool(stor8[caller]) != 1:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      32,
                      46,
                      0x735065726d697373696f6e65643a3a6f6e6c79416c6c6f7765644465706f736974732c206e6f7420616c6c6f7765,
                      mem[210 len 18]
      if bool(unknownb52a321f) != 1:
          revert with 0, 'DexStrategyV4::_deposit'
      if not unknown789139bc:
          require ext_code.size(unknownc89039c5Address)
          call unknownc89039c5Address.transferFrom(address from, address to, uint256 tokens) with:
               gas gas_remaining wei
              args caller, this.address, _param2
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0]
          if _param2 <= 0:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          34,
                          0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                          mem[198 len 30]
          require ext_code.size(stakingContractAddress)
          call stakingContractAddress.stake(uint256 stakeAmount) with:
               gas gas_remaining wei
              args _param2
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if not totalSupply:
              if _param2 + totalSupply < totalSupply:
                  revert with 0, 'SafeMath: addition overflow'
              totalSupply += _param2
              if _param2 + balanceOf[addr(_param1)] < balanceOf[addr(_param1)]:
                  revert with 0, 'SafeMath: addition overflow'
              balanceOf[addr(_param1)] += _param2
              log Transfer(
                    address from=_param2,
                    address to=0,
                    uint256 tokens=_param1)
          else:
              if totalDeposits * totalSupply / totalSupply != totalDeposits:
                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                              32,
                              33,
                              0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                              mem[197 len 31]
              if not totalDeposits * totalSupply:
                  if _param2 + totalSupply < totalSupply:
                      revert with 0, 'SafeMath: addition overflow'
                  totalSupply += _param2
                  if _param2 + balanceOf[addr(_param1)] < balanceOf[addr(_param1)]:
                      revert with 0, 'SafeMath: addition overflow'
                  balanceOf[addr(_param1)] += _param2
                  log Transfer(
                        address from=_param2,
                        address to=0,
                        uint256 tokens=_param1)
              else:
                  if not _param2:
                      if not totalDeposits:
                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      if (0 / totalDeposits) + totalSupply < totalSupply:
                          revert with 0, 'SafeMath: addition overflow'
                      totalSupply += 0 / totalDeposits
                      if (0 / totalDeposits) + balanceOf[addr(_param1)] < balanceOf[addr(_param1)]:
                          revert with 0, 'SafeMath: addition overflow'
                      balanceOf[addr(_param1)] += 0 / totalDeposits
                      log Transfer(
                            address from=(0 / totalDeposits),
                            address to=0,
                            uint256 tokens=_param1)
                  else:
                      if totalSupply * _param2 / _param2 != totalSupply:
                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                      32,
                                      33,
                                      0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                      mem[197 len 31]
                      if not totalDeposits:
                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      if (totalSupply * _param2 / totalDeposits) + totalSupply < totalSupply:
                          revert with 0, 'SafeMath: addition overflow'
                      totalSupply += totalSupply * _param2 / totalDeposits
                      if (totalSupply * _param2 / totalDeposits) + balanceOf[addr(_param1)] < balanceOf[addr(_param1)]:
                          revert with 0, 'SafeMath: addition overflow'
                      balanceOf[addr(_param1)] += totalSupply * _param2 / totalDeposits
                      log Transfer(
                            address from=(totalSupply * _param2 / totalDeposits),
                            address to=0,
                            uint256 tokens=_param1)
          if _param2 + totalDeposits < totalDeposits:
              revert with 0, 'SafeMath: addition overflow'
          totalDeposits += _param2
          log Deposit(
                address sender=_param2,
                uint256 value=_param1)
          stop
      require ext_code.size(stakingContractAddress)
      static call stakingContractAddress.0x8cc262 with:
              gas gas_remaining wei
             args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data <= unknown789139bc:
          require ext_code.size(unknownc89039c5Address)
          call unknownc89039c5Address.transferFrom(address from, address to, uint256 tokens) with:
               gas gas_remaining wei
              args caller, this.address, _param2
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0]
          if _param2 <= 0:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          34,
                          0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                          mem[198 len 30]
          require ext_code.size(stakingContractAddress)
          call stakingContractAddress.stake(uint256 stakeAmount) with:
               gas gas_remaining wei
              args _param2
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if not totalSupply:
              if _param2 + totalSupply < totalSupply:
                  revert with 0, 'SafeMath: addition overflow'
              totalSupply += _param2
              if _param2 + balanceOf[addr(_param1)] < balanceOf[addr(_param1)]:
                  revert with 0, 'SafeMath: addition overflow'
              balanceOf[addr(_param1)] += _param2
              log Transfer(
                    address from=_param2,
                    address to=0,
                    uint256 tokens=_param1)
          else:
              if totalDeposits * totalSupply / totalSupply != totalDeposits:
                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                              32,
                              33,
                              0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                              mem[197 len 31]
              if not totalDeposits * totalSupply:
                  if _param2 + totalSupply < totalSupply:
                      revert with 0, 'SafeMath: addition overflow'
                  totalSupply += _param2
                  if _param2 + balanceOf[addr(_param1)] < balanceOf[addr(_param1)]:
                      revert with 0, 'SafeMath: addition overflow'
                  balanceOf[addr(_param1)] += _param2
                  log Transfer(
                        address from=_param2,
                        address to=0,
                        uint256 tokens=_param1)
              else:
                  if not _param2:
                      if not totalDeposits:
                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      if (0 / totalDeposits) + totalSupply < totalSupply:
                          revert with 0, 'SafeMath: addition overflow'
                      totalSupply += 0 / totalDeposits
                      if (0 / totalDeposits) + balanceOf[addr(_param1)] < balanceOf[addr(_param1)]:
                          revert with 0, 'SafeMath: addition overflow'
                      balanceOf[addr(_param1)] += 0 / totalDeposits
                      log Transfer(
                            address from=(0 / totalDeposits),
                            address to=0,
                            uint256 tokens=_param1)
                  else:
                      if totalSupply * _param2 / _param2 != totalSupply:
                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                      32,
                                      33,
                                      0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                      mem[197 len 31]
                      if not totalDeposits:
                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      if (totalSupply * _param2 / totalDeposits) + totalSupply < totalSupply:
                          revert with 0, 'SafeMath: addition overflow'
                      totalSupply += totalSupply * _param2 / totalDeposits
                      if (totalSupply * _param2 / totalDeposits) + balanceOf[addr(_param1)] < balanceOf[addr(_param1)]:
                          revert with 0, 'SafeMath: addition overflow'
                      balanceOf[addr(_param1)] += totalSupply * _param2 / totalDeposits
                      log Transfer(
                            address from=(totalSupply * _param2 / totalDeposits),
                            address to=0,
                            uint256 tokens=_param1)
          if _param2 + totalDeposits < totalDeposits:
              revert with 0, 'SafeMath: addition overflow'
          totalDeposits += _param2
          log Deposit(
                address sender=_param2,
                uint256 value=_param1)
          stop
      require ext_code.size(stakingContractAddress)
      call stakingContractAddress.getReward() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      if not ext_call.return_data[0]:
          if not ext_call.return_data[0]:
              if not ext_call.return_data[0]:
                  if 0 <= ext_call.return_data[0]:
                      if ext_call.return_data / 2 <= 0:
                          revert with 0, 
                                      32,
                                      50,
                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                      mem[662 len 14]
                      require ext_code.size(unknownc89039c5Address)
                      static call unknownc89039c5Address.0xdfe1681 with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mem[608] = ext_call.return_data[12 len 20]
                      if rewardTokenAddress == mem[620 len 20]:
                          require ext_code.size(unknownc89039c5Address)
                          static call unknownc89039c5Address.token1() with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mem[704] = ext_call.return_data[12 len 20]
                          if rewardTokenAddress == mem[716 len 20]:
                              require ext_code.size(unknownf887ea40Address)
                              call unknownf887ea40Address.0xe8e33700 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataaddr(this.address), block.timestamp
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 96
                              if ext_call.return_data <= 0:
                                  revert with 0, 
                                              32,
                                              34,
                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                              Mask(239, 1, ext_call.return_data[0])
                              require ext_code.size(stakingContractAddress)
                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                   gas gas_remaining wei
                                  args ext_call.return_data[64]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              if ext_call.return_datatotalDeposits < totalDeposits:
                                  revert with 0, 'SafeMath: addition overflow'
                              totalDeposits += ext_call.return_data[64]
                              log 0xc7606d21: ext_call.return_data
              else:
                  if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                      revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                  if not unknown8aff733d * ext_call.return_data / 10000:
                      if 0 <= ext_call.return_data[0]:
                          if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                  revert with 0, 
                                              32,
                                              50,
                                              0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                              mem[662 len 14]
                              require ext_code.size(unknownc89039c5Address)
                              static call unknownc89039c5Address.0xdfe1681 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[608] = ext_call.return_data[12 len 20]
                              if rewardTokenAddress == mem[620 len 20]:
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.token1() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[704] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[716 len 20]:
                                      require ext_code.size(unknownf887ea40Address)
                                      call unknownf887ea40Address.0xe8e33700 with:
                                           gas gas_remaining wei
                                          args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 96
                                      if ext_call.return_data <= 0:
                                          revert with 0, 
                                                      32,
                                                      34,
                                                      0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                      Mask(239, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000))
                                      require ext_code.size(stakingContractAddress)
                                      call stakingContractAddress.stake(uint256 stakeAmount) with:
                                           gas gas_remaining wei
                                          args ext_call.return_data[64]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      if ext_call.return_datatotalDeposits < totalDeposits:
                                          revert with 0, 'SafeMath: addition overflow'
                                      totalDeposits += ext_call.return_data[64]
                                      log 0xc7606d21: ext_call.return_data
                  else:
                      require ext_code.size(rewardTokenAddress)
                      call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                           gas gas_remaining wei
                          args caller, unknown8aff733d * ext_call.return_data / 10000
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not ext_call.return_data[0]:
                          revert with 0, 'DexStrategyV4::_reinvest, reward'
                      if 0 <= ext_call.return_data[0]:
                          if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                  revert with 0, 
                                              32,
                                              50,
                                              0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                              mem[662 len 14]
                              require ext_code.size(unknownc89039c5Address)
                              static call unknownc89039c5Address.0xdfe1681 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[608] = ext_call.return_data[12 len 20]
                              if rewardTokenAddress == mem[620 len 20]:
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.token1() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[704] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[716 len 20]:
                                      require ext_code.size(unknownf887ea40Address)
                                      call unknownf887ea40Address.0xe8e33700 with:
                                           gas gas_remaining wei
                                          args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 96
                                      if ext_call.return_data <= 0:
                                          revert with 0, 
                                                      32,
                                                      34,
                                                      0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                      Mask(239, 1, ext_call.return_dataunknown8aff733d * ext_call.return_data / 10000))
                                      require ext_code.size(stakingContractAddress)
                                      call stakingContractAddress.stake(uint256 stakeAmount) with:
                                           gas gas_remaining wei
                                          args ext_call.return_data[64]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
          else:
              if unknown07677111 * ext_call.return_data / ext_call.return_dataunknown07677111:
                  revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[261 len 31]
              if not unknown07677111 * ext_call.return_data / 10000:
                  if not ext_call.return_data[0]:
                      if 0 <= ext_call.return_data[0]:
                          if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                  if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                      revert with 0, 
                                                  32,
                                                  50,
                                                  0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                  mem[662 len 14]
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.0xdfe1681 with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[608] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[620 len 20]:
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.token1() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[704] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[716 len 20]:
                                          require ext_code.size(unknownf887ea40Address)
                                          call unknownf887ea40Address.0xe8e33700 with:
                                               gas gas_remaining wei
                                              args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 96
                                          if ext_call.return_data <= 0:
                                              revert with 0, 
                                                          32,
                                                          34,
                                                          0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                          Mask(239, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000))
                                          require ext_code.size(stakingContractAddress)
                                          call stakingContractAddress.stake(uint256 stakeAmount) with:
                                               gas gas_remaining wei
                                              args ext_call.return_data[64]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          if ext_call.return_datatotalDeposits < totalDeposits:
                                              revert with 0, 'SafeMath: addition overflow'
                                          totalDeposits += ext_call.return_data[64]
                                          log 0xc7606d21: ext_call.return_data
                  else:
                      if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                          revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                      if not unknown8aff733d * ext_call.return_data / 10000:
                          if 0 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              if ext_call.return_datatotalDeposits < totalDeposits:
                                                  revert with 0, 'SafeMath: addition overflow'
                      else:
                          require ext_code.size(rewardTokenAddress)
                          call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                               gas gas_remaining wei
                              args caller, unknown8aff733d * ext_call.return_data / 10000
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              revert with 0, 'DexStrategyV4::_reinvest, reward'
                          if 0 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
              else:
                  require ext_code.size(rewardTokenAddress)
                  call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                       gas gas_remaining wei
                      args owner, unknown07677111 * ext_call.return_data / 10000
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if not ext_call.return_data[0]:
                      revert with 0, 'DexStrategyV4::_reinvest, admin'
                  if not ext_call.return_data[0]:
                      if 0 <= ext_call.return_data[0]:
                          if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                  if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                      revert with 0, 
                                                  32,
                                                  50,
                                                  0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                  mem[662 len 14]
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.0xdfe1681 with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[608] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[620 len 20]:
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.token1() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[704] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[716 len 20]:
                                          require ext_code.size(unknownf887ea40Address)
                                          call unknownf887ea40Address.0xe8e33700 with:
                                               gas gas_remaining wei
                                              args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 96
                                          if ext_call.return_data <= 0:
                                              revert with 0, 
                                                          32,
                                                          34,
                                                          0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                          Mask(239, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000))
                  else:
                      if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                          revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                      if not unknown8aff733d * ext_call.return_data / 10000:
                          if 0 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                      else:
                          require ext_code.size(rewardTokenAddress)
                          call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                               gas gas_remaining wei
                              args caller, unknown8aff733d * ext_call.return_data / 10000
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              revert with 0, 'DexStrategyV4::_reinvest, reward'
                          if 0 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
      else:
          if unknown5ea682ea * ext_call.return_data / ext_call.return_dataunknown5ea682ea:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          33,
                          0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                          mem[197 len 31]
          if not unknown5ea682ea * ext_call.return_data / 10000:
              if ext_call.return_data[0]:
                  if unknown07677111 * ext_call.return_data / ext_call.return_dataunknown07677111:
                      revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[261 len 31]
                  if not unknown07677111 * ext_call.return_data / 10000:
                      if not ext_call.return_data[0]:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              if ext_call.return_datatotalDeposits < totalDeposits:
                                                  revert with 0, 'SafeMath: addition overflow'
                      else:
                          if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                              revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                          if not unknown8aff733d * ext_call.return_data / 10000:
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >= 96
                                                  if ext_call.return_data <= 0:
                                                      revert with 0, 
                                                                  32,
                                                                  34,
                                                                  0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                                  Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                                  require ext_code.size(stakingContractAddress)
                                                  call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                       gas gas_remaining wei
                                                      args ext_call.return_data[64]
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require ext_code.size(rewardTokenAddress)
                              call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                                   gas gas_remaining wei
                                  args caller, unknown8aff733d * ext_call.return_data / 10000
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not ext_call.return_data[0]:
                                  revert with 0, 'DexStrategyV4::_reinvest, reward'
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >= 96
                                                  if ext_call.return_data <= 0:
                                                      revert with 0, 
                                                                  32,
                                                                  34,
                                                                  0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                                  Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                  else:
                      require ext_code.size(rewardTokenAddress)
                      call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                           gas gas_remaining wei
                          args owner, unknown07677111 * ext_call.return_data / 10000
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not ext_call.return_data[0]:
                          revert with 0, 'DexStrategyV4::_reinvest, admin'
                      if not ext_call.return_data[0]:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                      else:
                          if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                              revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                          if not unknown8aff733d * ext_call.return_data / 10000:
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >= 96
                          else:
                              require ext_code.size(rewardTokenAddress)
                              call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                                   gas gas_remaining wei
                                  args caller, unknown8aff733d * ext_call.return_data / 10000
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not ext_call.return_data[0]:
                                  revert with 0, 'DexStrategyV4::_reinvest, reward'
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
              else:
                  if not ext_call.return_data[0]:
                      if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                          if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                              if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) / 2 <= 0:
                                  revert with 0, 
                                              32,
                                              50,
                                              0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                              mem[662 len 14]
                              require ext_code.size(unknownc89039c5Address)
                              static call unknownc89039c5Address.0xdfe1681 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[608] = ext_call.return_data[12 len 20]
                              if rewardTokenAddress == mem[620 len 20]:
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.token1() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[704] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[716 len 20]:
                                      require ext_code.size(unknownf887ea40Address)
                                      call unknownf887ea40Address.0xe8e33700 with:
                                           gas gas_remaining wei
                                          args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 96
                                      if ext_call.return_data <= 0:
                                          revert with 0, 
                                                      32,
                                                      34,
                                                      0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                      Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000))
                                      require ext_code.size(stakingContractAddress)
                                      call stakingContractAddress.stake(uint256 stakeAmount) with:
                                           gas gas_remaining wei
                                          args ext_call.return_data[64]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      if ext_call.return_datatotalDeposits < totalDeposits:
                                          revert with 0, 'SafeMath: addition overflow'
                                      totalDeposits += ext_call.return_data[64]
                                      log 0xc7606d21: ext_call.return_data
                  else:
                      if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                          revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                      if not unknown8aff733d * ext_call.return_data / 10000:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              if ext_call.return_datatotalDeposits < totalDeposits:
                                                  revert with 0, 'SafeMath: addition overflow'
                      else:
                          require ext_code.size(rewardTokenAddress)
                          call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                               gas gas_remaining wei
                              args caller, unknown8aff733d * ext_call.return_data / 10000
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              revert with 0, 'DexStrategyV4::_reinvest, reward'
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
          else:
              require ext_code.size(rewardTokenAddress)
              call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                   gas gas_remaining wei
                  args devAddr, unknown5ea682ea * ext_call.return_data / 10000
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'DexStrategyV4::_reinvest, dev'
              if not ext_call.return_data[0]:
                  if not ext_call.return_data[0]:
                      if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                          if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                              if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) / 2 <= 0:
                                  revert with 0, 
                                              32,
                                              50,
                                              0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                              mem[662 len 14]
                              require ext_code.size(unknownc89039c5Address)
                              static call unknownc89039c5Address.0xdfe1681 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[608] = ext_call.return_data[12 len 20]
                              if rewardTokenAddress == mem[620 len 20]:
                                  require ext_code.size(unknownc89039c5Address)
                                  static call unknownc89039c5Address.token1() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[704] = ext_call.return_data[12 len 20]
                                  if rewardTokenAddress == mem[716 len 20]:
                                      require ext_code.size(unknownf887ea40Address)
                                      call unknownf887ea40Address.0xe8e33700 with:
                                           gas gas_remaining wei
                                          args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 96
                                      if ext_call.return_data <= 0:
                                          revert with 0, 
                                                      32,
                                                      34,
                                                      0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                      Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000))
                                      require ext_code.size(stakingContractAddress)
                                      call stakingContractAddress.stake(uint256 stakeAmount) with:
                                           gas gas_remaining wei
                                          args ext_call.return_data[64]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                  else:
                      if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                          revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                      if not unknown8aff733d * ext_call.return_data / 10000:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                      else:
                          require ext_code.size(rewardTokenAddress)
                          call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                               gas gas_remaining wei
                              args caller, unknown8aff733d * ext_call.return_data / 10000
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              revert with 0, 'DexStrategyV4::_reinvest, reward'
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
              else:
                  if unknown07677111 * ext_call.return_data / ext_call.return_dataunknown07677111:
                      revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[261 len 31]
                  if unknown07677111 * ext_call.return_data / 10000:
                      require ext_code.size(rewardTokenAddress)
                      call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                           gas gas_remaining wei
                          args owner, unknown07677111 * ext_call.return_data / 10000
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not ext_call.return_data[0]:
                          revert with 0, 'DexStrategyV4::_reinvest, admin'
                      if not ext_call.return_data[0]:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                      else:
                          if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                              revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                          if not unknown8aff733d * ext_call.return_data / 10000:
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                          else:
                              require ext_code.size(rewardTokenAddress)
                              call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                                   gas gas_remaining wei
                                  args caller, unknown8aff733d * ext_call.return_data / 10000
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not ext_call.return_data[0]:
                                  revert with 0, 'DexStrategyV4::_reinvest, reward'
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                  else:
                      if not ext_call.return_data[0]:
                          if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                              if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                  if 0 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                      if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) / 2 <= 0:
                                          revert with 0, 
                                                      32,
                                                      50,
                                                      0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                      mem[662 len 14]
                                      require ext_code.size(unknownc89039c5Address)
                                      static call unknownc89039c5Address.0xdfe1681 with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[608] = ext_call.return_data[12 len 20]
                                      if rewardTokenAddress == mem[620 len 20]:
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.token1() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[704] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[716 len 20]:
                                              require ext_code.size(unknownf887ea40Address)
                                              call unknownf887ea40Address.0xe8e33700 with:
                                                   gas gas_remaining wei
                                                  args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 96
                                              if ext_call.return_data <= 0:
                                                  revert with 0, 
                                                              32,
                                                              34,
                                                              0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                              Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000))
                                              require ext_code.size(stakingContractAddress)
                                              call stakingContractAddress.stake(uint256 stakeAmount) with:
                                                   gas gas_remaining wei
                                                  args ext_call.return_data[64]
                      else:
                          if unknown8aff733d * ext_call.return_data / ext_call.return_dataunknown8aff733d:
                              revert with 0, 32, 33, 0x79536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[325 len 31]
                          if not unknown8aff733d * ext_call.return_data / 10000:
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >= 96
                                                  if ext_call.return_data <= 0:
                                                      revert with 0, 
                                                                  32,
                                                                  34,
                                                                  0x73446578537472617465677956343a3a5f7374616b654465706f736974546f6b656e,
                                                                  Mask(239, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000))
                          else:
                              require ext_code.size(rewardTokenAddress)
                              call rewardTokenAddress.transfer(address to, uint256 tokens) with:
                                   gas gas_remaining wei
                                  args caller, unknown8aff733d * ext_call.return_data / 10000
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not ext_call.return_data[0]:
                                  revert with 0, 'DexStrategyV4::_reinvest, reward'
                              if unknown5ea682ea * ext_call.return_data / 10000 <= ext_call.return_data[0]:
                                  if unknown07677111 * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000):
                                      if unknown8aff733d * ext_call.return_data / 10000 <= ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000):
                                          if ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000) / 2 <= 0:
                                              revert with 0, 
                                                          32,
                                                          50,
                                                          0x64446578537472617465677956343a3a5f636f6e76657274526577617264546f6b656e73546f4465706f736974546f6b656e,
                                                          mem[662 len 14]
                                          require ext_code.size(unknownc89039c5Address)
                                          static call unknownc89039c5Address.0xdfe1681 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          mem[608] = ext_call.return_data[12 len 20]
                                          if rewardTokenAddress == mem[620 len 20]:
                                              require ext_code.size(unknownc89039c5Address)
                                              static call unknownc89039c5Address.token1() with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >= 32
                                              mem[704] = ext_call.return_data[12 len 20]
                                              if rewardTokenAddress == mem[716 len 20]:
                                                  require ext_code.size(unknownf887ea40Address)
                                                  call unknownf887ea40Address.0xe8e33700 with:
                                                       gas gas_remaining wei
                                                      args addr(ext_call.return_data), addr(ext_call.return_data), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), Mask(255, 1, ext_call.return_dataunknown5ea682ea * ext_call.return_data / 10000) - (unknown07677111 * ext_call.return_data / 10000) - (unknown8aff733d * ext_call.return_data / 10000)), 0, 0, addr(this.address), block.timestamp
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]


