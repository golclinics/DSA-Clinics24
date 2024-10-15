import 'package:fizz_buzz/fizz.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(const MainApp());
}

class MainApp extends StatelessWidget {
  const MainApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Center(
        child: Scaffold(
          appBar: AppBar(title: const Text('FizzBuzz'),),
          body:  FizzBuzz(),
        ),  
      ),
    );
  }
}
