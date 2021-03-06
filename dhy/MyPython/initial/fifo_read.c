#include <sys/types.h>  
#include <sys/stat.h>  
#include <errno.h>  
#include <fcntl.h>  
#include <stdio.h>  
#include <stdlib.h>  
#include <string.h>  
#define FIFO "./p1"  
  
main(int argc,char** argv)  
{  
    char buf_r[100];  
    int  fd;  
    int  nread;  
      
    /*创建有名管道,并设置相应的权限*/  
    if((mkfifo(FIFO,O_CREAT|O_EXCL)<0)&&(errno!=EEXIST))  
        printf("cannot create fifoserver\n");  
    printf("Preparing for reading bytes...\n");  
      
    memset(buf_r,0,sizeof(buf_r));  
    /*打开有名管道，并设置非阻塞标志*/  
    fd=open(FIFO,O_RDONLY,0);  
    if(fd==-1)  
    {  
        perror("open");  
        exit(1);      
    }  
   printf("open pipe read successfully!\n");
    while(1)  
    {  
        memset(buf_r,0,sizeof(buf_r));  
        /*读取管道中的字符串*/  
        if((nread=read(fd,buf_r,44))==-1){  
            if(errno==EAGAIN)  
                printf("no data yet\n");  
        }  
	if(strlen(buf_r) != 0)
        printf("read %s from FIFO\n",buf_r);  
 
    }     
    pause();  
    unlink(FIFO);  
}  
