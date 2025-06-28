# HyperEVM micro buy bot

A trading bot that automatically buys tokens on the HyperEVM blockchain using micro-transactions of HYPE every 5 seconds (configurable).

## Description

This bot automatically purchases tokens using micro-transactions of HYPE (0.00000001 HYPE by default) every 5 seconds (configurable) on the HyperEVM blockchain.

## Features

- Buys tokens automatically every 5 seconds (configurable)
- Uses micro-transactions of HYPE (configurable)
- Works on HyperEVM blockchain
- Easy to configure

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

Edit `hype_swap_bot.py` and set:
- **PRIVATE_KEY**: Your wallet's private key
- **TOKEN_ADDRESS**: The token you want to buy
- **ROUTER_ADDRESS**: The HyperswapRouter address
- **AMOUNT_HYPE**: Amount of HYPE to use (default: 0.00000001)
- **FREQUENCY**: Time between purchases in seconds (default: 5)

## Usage

Run the bot:
```bash
python hype_swap_bot.py
```

## Requirements

- Python 3.7+
- web3==6.15.1
- eth-account==0.11.0

## Warning

⚠️ Never share your private key. This bot is for educational purposes only. 
