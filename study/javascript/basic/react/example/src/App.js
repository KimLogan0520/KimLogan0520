import logo from './logo.svg';
import './App.css';
import { useState } from 'react';

function MyButton({count, onClick}) {
    // const [count, setCount] = useState(0);

    /**
     * Notice how each button “remembers” its own count state and doesn’t affect other buttons.
     */
    // function handleClick() {
    //     alert('You clicked me!');
        // setCount(count + 1);
    // }

    return (
        /**
         * 괄호를 추가할 필요가 없다. ex. handleClick() 처럼...
         * 사용자가 버튼 클릭시, 응답이 이벤트 핸들러를 호출함!!
         */
        <button onClick={onClick}>
            I'm a onClick
            Clicked {count} times!
        </button>
    )
}

const user = {
    name: 'Hedy Lamarr',
    imageUrl: 'https://i.imgur.com/yXOvdOSs.jpg',
    imageSize: 90,
}

/**
 * The export default keywords specify the main component in the file.
 */
export default function MyApp() {
    const [count, setCount] = useState(0);

    function handleClick() {
        setCount(count + 1);
    }

    const products = [
        { title: 'Cabbage', isFruit: false, id: 1 },
        { title: 'Garlic', isFruit: false, id: 2 },
        { title: 'Apple', isFruit: true, id: 3 },
    ]

    /**
     * li 태그는 "key" 속성을 갖는다.
     * Usually, a key should be coming from your data, such as a database ID.
     * React uses your keys to know what happened if you later insert, delete, or reorder the items.
     */
    const listItems = products.map(products =>
        <li
            key={products.id}
            style={{
                color: products.isFruit ? 'magenta' : 'darkgreen'
            }}
        >
            {products.title}
        </li>
    )

    return (
    // <div className="App">
    //   <header className="App-header">
    //     <img src={logo} className="App-logo" alt="logo" />
    //     <p>
    //       Edit <code>src/App.js</code> and save to reload.
    //     </p>
    //     <a
    //       className="App-link"
    //       href="https://reactjs.org"
    //       target="_blank"
    //       rel="noopener noreferrer"
    //     >
    //       Learn React
    //     </a>
    //   </header>
    // </div>
    <div className="App">
        <h1>Welcome to my app!</h1>
        <MyButton count={count} onClick={handleClick}/>
        <MyButton count={count} onClick={handleClick}/>

        <hr />

        <ul>
            {listItems}
        </ul>

        <hr />

        <img
            src={user.imageUrl}
            alt={'Photo of ' + user.name}
            style={{
                width: user.imageSize,
                height: user.imageSize
            }}
        />
    </div>
  );
}
