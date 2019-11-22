#include <stdio.h>
#include <sys/socket.h> 
#include <arpa/inet.h>
#include <sys/stat.h>
#include <sys/sendfile.h>
#include <fcntl.h>
#include <stdlib.h>
#include <string.h>

#define FILENAME 	"a.txt"
#define SERVER_IP 	"192.168.1.66"
#define SERVER_PORT 	21

int main(int argc , char **argv)
{
	int 	socket_desc;
	struct 	sockaddr_in server;
	char 	request_msg[BUFSIZ],
		reply_msg[BUFSIZ];

	// Variables for the file being received
	int	file_size,
		file_desc;
	char	*data;
		
	socket_desc = socket(AF_INET, SOCK_STREAM, 0);
	if (socket_desc == -1)
	{
		perror("Could not create socket");
		return 1;
	}

	server.sin_addr.s_addr = inet_addr(SERVER_IP);
	server.sin_family = AF_INET;
	server.sin_port = htons(SERVER_PORT);

	// Connect to server
	if (connect(socket_desc, (struct sockaddr *)&server, sizeof(server)) < 0)
	{
		perror("Connection failed");
		return 1;
	}


	return 0;
}
