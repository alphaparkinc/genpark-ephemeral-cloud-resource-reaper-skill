from client import EphemeralCloudResourceReaperClient

def main():
    client = EphemeralCloudResourceReaperClient()
    res = client.reap_abandoned_cloud_resources(12, {'managed-by': 'ai-sandbox'})
    print('Cloud Resource Reaper: ' + res['reaper_execution_id'] + ' (' + str(res['idle_resources_discovered_count']) + ' resources reaped)')
    print('GPU Instances Terminated: ' + str(res['idle_gpu_instances_terminated_count']) + ' | Monthly Savings: $' + str(res['projected_monthly_cost_saved_usd']))
    print('Manifest URL: ' + res['reaper_audit_manifest_url'])

if __name__ == '__main__':
    main()
