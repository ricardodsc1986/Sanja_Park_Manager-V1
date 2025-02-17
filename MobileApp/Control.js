
import React, { useState, useEffect } from 'react';
import { View, Text, Button, FlatList } from 'react-native';

const Control = () => {
    const [veiculos, setVeiculos] = useState([]);

    useEffect(() => {
        fetch('http://localhost:5000/api/veiculos')
            .then(response => response.json())
            .then(data => setVeiculos(data));
    }, []);

    return (
        <View>
            <Text>Estacionamento - Controle de Veículos</Text>
            <FlatList
                data={veiculos}
                renderItem={({ item }) => (
                    <View>
                        <Text>{item.placa}</Text>
                        <Text>{item.entrada}</Text>
                        <Text>{item.saida}</Text>
                    </View>
                )}
                keyExtractor={(item) => item.placa}
            />
        </View>
    );
};

export default Control;
    