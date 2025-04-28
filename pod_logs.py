from kubernetes import client, config

# kubeconfig 로드
config.load_kube_config()

v1 = client.CoreV1Api()
namespace = "django-app"  # 원하는 네임스페이스 이름

try:
    pods = v1.list_namespaced_pod(namespace=namespace)
    for pod in pods.items:
        pod_name = pod.metadata.name
        print(f"\n📦 {pod_name} 로그:")
        print("-" * 50)
        try:
            log = v1.read_namespaced_pod_log(name=pod_name, namespace=namespace, tail_lines=100)
            print(log)
        except client.exceptions.ApiException as e:
            print(f"❌ {pod_name} 로그 가져오기 실패: {e.reason}")
except client.exceptions.ApiException as e:
    print(f"❌ 네임스페이스에서 Pod 목록 가져오기 실패: {e.reason}")

