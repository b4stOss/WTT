# What To Trade (WTT) 🚀

WTT is a powerful cryptocurrency analysis tool that helps traders identify potential trading opportunities by analyzing technical indicators across the top 100 cryptocurrencies by market cap.

## Features ✨

- **Real-time Analysis**: Fetches and analyzes current market data for the top 100 cryptocurrencies
- **Multiple Technical Indicators**:
  - RSI (Relative Strength Index) - 14 periods
  - Moving Average with customizable periods
  - Combined analysis (RSI + MA)
- **Stablecoin Filtering**: Automatically excludes stablecoins from analysis
- **Web Interface**: Simple and intuitive web interface for easy interaction
- **Async Processing**: Efficient data fetching and processing using Python's asyncio

## Installation 🛠️

1. Clone the repository:
```bash
git clone https://github.com/yourusername/WTT.git
cd WTT
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your settings in `config.json`:
```json
{
    "stablecoins": ["USDT", "USDC", "DAI", "UST", "BUSD"]
}
```

## Usage 💡

1. Start the web server:
```bash
python -m WTT
```

2. Open your browser and navigate to `http://localhost:8080`

3. Select your preferred indicator:
   - MA (Moving Average)
   - RSI (Relative Strength Index)
   - ALL (Combined Analysis)

4. Enter the period for MA analysis (not required for RSI)

5. Click "Check" to get your analysis results

## API Integration 🔌

WTT uses the CryptoCompare API for market data. The current implementation includes rate limiting and efficient data fetching through asynchronous requests.

## Contributing 🤝

Contributions are welcome! Feel free to submit a Pull Request.

## License 📝

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments 🙏

- [CryptoCompare](https://min-api.cryptocompare.com/) for providing the cryptocurrency market data API
- Built with Python, aiohttp, and Pandas

## Author ✍️
B4stOss

---

*Note: This tool is for educational purposes only. Always do your own research before making investment decisions.*
