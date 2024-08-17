# DAppSC6113
## 1. Write contract on Remix and compile, then write a html according to solidity 
file: templates/w1 storage.sol  
html: pay attention to const contractABI(copy ABI from Remix Solidity Complier) and ContractAddress(from Deploy & run transactions -> Deployed/Unpinned Contracts -> STORE_MONEY AT copy that address)
## 2. Get MetaMask account and some SepoliaETH
free SepoliaETH from website:  
https://cloud.google.com/application/web3/faucet/ethereum/sepolia  
https://faucets.chain.link/  
few is enough.
## 3. Download 
install node  
npm install http-server -g  
npm install web3  
npm install ethers  
npm start    
http-server  
(where to command where need .html in the same folder/path)
## 4. Connect MetaMask with website
check if store and view function work successfully
## 5. Use Render to Deploy your DApp
first upload html to open repository and add app.py & requirements.txt  
Render new a Web Service, Noted that choose Python3 not Doker  
select repository, free instance type  
Noted:   
build command: pip install -r requirements.txt  
start command: gunicorn app:app  
Deploy! Done!  
    
### Thanks to my friend natalieybl.  
2024.8.17   
