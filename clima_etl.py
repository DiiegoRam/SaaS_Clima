import random
import datetime
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# --- 1. EXTRAER (Simulación local para evitar bloqueos de API) ---
print("Generando lectura del clima para Acapulco...")
temperatura_simulada = round(random.uniform(28.0, 35.0), 1)
humedad_simulada = random.randint(65, 90)
condiciones = ["Soleado", "Parcialmente Nublado", "Lluvia ligera", "Caluroso"]
condicion_simulada = random.choice(condiciones)

# --- 2. TRANSFORMAR (Estructurar en formato JSON) ---
documento = {
    "timestamp": datetime.datetime.utcnow().isoformat(),
    "ciudad": "Acapulco",
    "temperatura": temperatura_simulada,
    "humedad": humedad_simulada,
    "condicion": condicion_simulada
}
print(f"Datos listos: {documento['temperatura']}°C, {documento['humedad']}% humedad")

# --- 3. CARGAR (Enviar a tu IBM Cloudant) ---
API_KEY_CLOUDANT = "KfqjMzwhVi4PEYx9a2XWmP3xy4BW61d9J5M2ZJBOr5UV"
URL_CLOUDANT = "https://b606a9b6-48d2-48b5-b3be-142f01ba38c9-bluemix.cloudantnosqldb.appdomain.cloud"

print("Conectando a IBM Cloudant...")
authenticator = IAMAuthenticator(API_KEY_CLOUDANT)
cliente = CloudantV1(authenticator=authenticator)
cliente.set_service_url(URL_CLOUDANT)

# Enviar el documento a la base de datos "clima_acapulco" que ya creamos
cliente.post_document(
    db='clima_acapulco',
    document=documento
).get_result()

print("¡Éxito! El registro se guardó en tu base de datos de IBM Cloud.")