import { useEffect } from "react";
import { useState } from "react";

function App() {
  const [loading, setLoading] = useState(true);
  const [coins, setCoins] = useState([]);
  const [money, setMoney] = useState(0);
  const [price, setPrice] = useState(1);
  const onMoney = (event) => {
    setMoney(event.target.value);
  };
  const onChange = (event) => {
    let index = event.target.selectedIndex;
    let coin = coins[index];
    setPrice(coin.quotes.USD.price);
  };
  useEffect(() => {
    fetch("https://api.coinpaprika.com/v1/tickers")
      .then((response) => response.json())
      .then((json) => {
        setCoins(json);
        setLoading(false);
        setPrice(json[0].quotes.USD.price);
      });
  }, []);
  // console.log(price)
  return (
    <div>
      <h1>The Coins! ({coins.length})</h1>

      {loading ? (
        <strong>Loading...</strong>
      ) : (
        <div>
          <select onChange={onChange}>
            {coins.map((coin) => (
              <option key={coin.id}>
                {coin.name} ({coin.symbol}) : {coin.quotes.USD.price} USD
              </option>
            ))}
          </select>
          <input
            onChange={onMoney}
            value={money}
            type="number"
            placeholder="몇 원 사용 가능?"
          ></input>
          <h3>
            {money}원 있으면 {Math.floor((money * 0.00076) / price)}개 구입 가능
          </h3>
        </div>
      )}
    </div>
  );
}

export default App;
