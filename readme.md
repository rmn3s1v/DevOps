Проброс Grafana
kubectl port-forward -n monitoring svc/prometheus-grafana 3000:80 --address 0.0.0.0

Просмотр мониторинга (grafana, prometheus)
kubectl get pods -n monitoring

Просмотр мониторинга devops
kubectl get pods -n devops

Для получения external ip
kubectl get svc -n devops

Запуск Yandex Tank
docker run --rm -it \
  -v $(pwd):/var/loadtest \
  --net host \
  yandex/yandex-tank \
  -c /var/loadtest/load.yaml

Отслеживание нагрузки
watch kubectl get hpa,deploy,pods -n devops

Прямое подключение к БД
kubectl exec -it mongo-55b9b9b7db-4f6ks -n devops -- mongosh


DevOps1234567_
