from __future__ import print_function, unicode_literals

from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint

import socket
import sys

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})

class Speaker():

    def repeatString(self, text, many):
        assert isinstance(many, int)
        for i in range(3):
            print(text)

class Server():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the port
    server_address = ('localhost', 10000)
    print('starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)

    while True:
        print('\nwaiting to receive message')
        data, address = sock.recvfrom(4096)

        print('received {} bytes from {}'.format(
            len(data), address))
        print(data)

        if data:
            sent = sock.sendto(data, address)
            print('sent {} bytes back to {}'.format(
                sent, address))

def main():
    options = [
        {
            'type': 'checkbox',
            'message': 'Select server options',
            'name': 'options selected',
            'choices': [
                Separator('= Connection Type ='),
                {
                    'name': 'UDP',
                    'checked': True
                },
                {
                    'name': 'TCP',
                    'disabled': 'not implemented yet'
                },
                Separator('= Packet Size (if TCP not relevant) ='),
                {
                    'name': '100 kB packets',
                    'checked': True
                },
                {
                    'name': '256 kB packets'
                },
                {
                    'name': '1024 kB packets'
                },
                Separator('= Packet Loss % ='),
                {
                    'name': '0%',
                    'checked': True
                },
                {
                    'name': '33%'
                },
                {
                    'name': '50%'
                },
                {
                    'name': '75%'
                },
                {
                    'name': 'Random between 10-99%'
                },
                Separator('= Forward Error Correction Method ='),
                {
                    'name': 'No FEC',
                    'checked': True
                },
                {
                    'name': 'Triple Buffer FEC',
                },
                {
                    'name': 'XOR FEC'
                }
            ],
            'validate': lambda answer: 'You must choose at least one topping.' \
                if len(answer) == 0 else True
        }
    ]

    answers = prompt(options, style=style)
    pprint(answers)

    if (answers[0] == 'UDP'):
        serv = Server()
    talker = Speaker()
    talker.repeatString("hei", 3)

if __name__ == '__main__':
    main()