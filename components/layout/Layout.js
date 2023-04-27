import React from 'react';
import { Text, Window } from 'proton-native';

export default function Layout(){
    return (
    <Window style={{ width: 500, height: 300, backgroundColor: "black" }}>
        <Text style={{backgroundColor: 'white', fontSize: 20}}>This will be the smart mirror</Text>
    </Window>
  )
}
