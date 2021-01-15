# cat-pi-monitor
Monitor your cat in local network by Raspberry PI Camera and upload it to cloud server.

### gRPC

```shell
python3 -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I. monitor.proto
```

## TODO list

- [ ] A web interface for 