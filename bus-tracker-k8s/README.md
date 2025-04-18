# Kubernetes Setup for Bus Tracker App

## Step 1: Deploy the Application
```bash
kubectl apply -f deployment.yaml
```

## Step 2: Expose the Application
```bash
kubectl apply -f service.yaml
```

## Step 3: Access the Application
### On Minikube:
```bash
minikube service bus-tracker-service
```

### On Cloud (EKS/GKE/AKS):
Wait for the external IP and hit:
```
http://<EXTERNAL-IP>/bus/location
```
