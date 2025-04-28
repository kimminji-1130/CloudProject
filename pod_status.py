from kubernetes import client, config

# kubeconfig 로드
config.load_kube_config()

v1 = client.CoreV1Api()

print("📡 현재 모든 네임스페이스의 Pod 상태:")
pods = v1.list_pod_for_all_namespaces(watch=False)
for pod in pods.items:
    print(f"{pod.metadata.namespace}\t{pod.metadata.name}\t{pod.status.phase}")

