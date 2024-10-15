import 'package:flutter/material.dart';

class FizzBuzz extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: ListView.builder(
        itemCount: 100,
        itemBuilder: (context, index) {
          int number = index + 1;
          String text;
      
          if (number % 3 == 0 && number % 5 == 0) {
            text = 'FizzBuzz';
          } else if (number % 3 == 0) {
            text = 'Fizz';
          } else if (number % 5 == 0) {
            text = 'Buzz';
          } else {
            text = '$number';
          }
      
          return ListTile(
            title: Text(text),
          );
        },
      ),
    );
  }
}
