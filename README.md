# cat-pi-monitor
Monitor your cat in local network by Raspberry PI Camera and upload it to cloud server.

### gRPC

```shell
python3 -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I. monitor.proto
```

## TODO list

- [ ] A web interface for 
    - [ ] 显示已保存的视频
- [ ] 一个队列可以保存一定长度的视频数据
- [ ] 有人访问的时候客户端才上传数据