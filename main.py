import paramiko
import threading

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy)
client.connect('localhost', username=, password=)
# _, std_out, std_err = client.exec_command('python3 /mnt/share/Projects/Python/paramiko/tmp.py', get_pty=True)
_, std_out, std_err = client.exec_command('python3 /mnt/share/Projects/Python/paramiko/tmp.py')


def reader(stream, prefix):
    # for line in iter(stream.readline, ''):
    #     print(f'{prefix} - {line}')
    # data = True
    # while data:
    #     data = stream.channel.recv(1)
    #     print(f'{prefix} - {data.splitlines()}')
    for line in stream:
        print(f'{prefix} - {line}')


# out_printer = threading.Thread(target=reader, args=(std_out, 'from output'))
err_printer = threading.Thread(target=reader, args=(std_err, 'from error'))

# out_printer.start()
err_printer.start()

# print(f'out: {std_out.readlines()}')
# print(f'err: {std_err.readlines()}')

print('End')
