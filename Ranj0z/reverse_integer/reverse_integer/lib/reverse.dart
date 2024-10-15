import 'package:flutter/material.dart';

class ReverseInteger extends StatelessWidget {
  const ReverseInteger({super.key});
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        children: [
          Text("Text field"),
          TextButton(
              onPressed: () {
                // showModalBottomSheet(
                //     context: context,
                //     builder: (Buildecontext) {
                //       return Container(
                //         child: ,
                //       );
                //     });
              },
              child: Text('Input integer')),
        ],
      ),
    );
  }
}
