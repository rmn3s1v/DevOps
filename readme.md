kubectl port-forward -n monitoring svc/prometheus-grafana 3000:80 --address 0.0.0.0

docker run --rm -it \
  -v $(pwd):/var/loadtest \
  --net host \
  yandex/yandex-tank \
  -c /var/loadtest/load.yaml

watch kubectl get hpa,deploy,pods -n devops

kubectl exec -it mongo-55b9b9b7db-4f6ks -n devops -- mongo
