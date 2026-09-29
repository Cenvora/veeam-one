"""Contains all the data models used in inputs/outputs"""

from .access_token_role import AccessTokenRole
from .agent_backup_job_info import AgentBackupJobInfo
from .agent_backup_job_info_page import AgentBackupJobInfoPage
from .agent_backup_job_platform import AgentBackupJobPlatform
from .agent_backup_job_type import AgentBackupJobType
from .agent_policy_child_job_info import AgentPolicyChildJobInfo
from .agent_policy_child_job_info_page import AgentPolicyChildJobInfoPage
from .agent_policy_info import AgentPolicyInfo
from .agent_policy_info_page import AgentPolicyInfoPage
from .alarm_assignment import AlarmAssignment
from .alarm_assignment_object_type import AlarmAssignmentObjectType
from .alarm_source import AlarmSource
from .alarm_source_object_type import AlarmSourceObjectType
from .alarm_status import AlarmStatus
from .alarm_template_info import AlarmTemplateInfo
from .alarm_template_info_page import AlarmTemplateInfoPage
from .alarm_template_type import AlarmTemplateType
from .application_backup_job_info import ApplicationBackupJobInfo
from .application_backup_job_info_page import ApplicationBackupJobInfoPage
from .application_backup_job_status import ApplicationBackupJobStatus
from .application_info import ApplicationInfo
from .application_info_page import ApplicationInfoPage
from .application_job_platform import ApplicationJobPlatform
from .application_platform import ApplicationPlatform
from .application_transaction_log_backup_job_info import ApplicationTransactionLogBackupJobInfo
from .application_transaction_log_backup_job_info_page import ApplicationTransactionLogBackupJobInfoPage
from .archive_tier_extent_info import ArchiveTierExtentInfo
from .archive_tier_extent_info_page import ArchiveTierExtentInfoPage
from .assign_type import AssignType
from .async_task_state import AsyncTaskState
from .async_task_status import AsyncTaskStatus
from .authentication_create_token_data_body import AuthenticationCreateTokenDataBody
from .authentication_create_token_data_body_grant_type import AuthenticationCreateTokenDataBodyGrantType
from .authentication_create_token_files_body import AuthenticationCreateTokenFilesBody
from .authentication_create_token_files_body_grant_type import AuthenticationCreateTokenFilesBodyGrantType
from .authentication_revoke_token_data_body import AuthenticationRevokeTokenDataBody
from .authentication_revoke_token_files_body import AuthenticationRevokeTokenFilesBody
from .backup_agent_info import BackupAgentInfo
from .backup_agent_info_page import BackupAgentInfoPage
from .backup_agent_status import BackupAgentStatus
from .backup_cluster_info import BackupClusterInfo
from .backup_cluster_info_page import BackupClusterInfoPage
from .backup_copy_child_job_info import BackupCopyChildJobInfo
from .backup_copy_child_job_info_page import BackupCopyChildJobInfoPage
from .backup_copy_job_info import BackupCopyJobInfo
from .backup_copy_job_info_page import BackupCopyJobInfoPage
from .backup_job_status import BackupJobStatus
from .backup_platform_type import BackupPlatformType
from .backup_proxy_info import BackupProxyInfo
from .backup_proxy_info_page import BackupProxyInfoPage
from .backup_proxy_state import BackupProxyState
from .backup_proxy_transport_mode import BackupProxyTransportMode
from .backup_proxy_type import BackupProxyType
from .backup_repository_info import BackupRepositoryInfo
from .backup_repository_info_page import BackupRepositoryInfoPage
from .backup_repository_type import BackupRepositoryType
from .backup_server_connection_state import BackupServerConnectionState
from .backup_server_info import BackupServerInfo
from .backup_server_info_page import BackupServerInfoPage
from .backup_to_tape_job_info import BackupToTapeJobInfo
from .backup_to_tape_job_info_page import BackupToTapeJobInfoPage
from .best_practice_check_status import BestPracticeCheckStatus
from .best_practice_group import BestPracticeGroup
from .best_practice_info import BestPracticeInfo
from .best_practice_info_page import BestPracticeInfoPage
from .best_practice_status import BestPracticeStatus
from .business_view_category_info import BusinessViewCategoryInfo
from .business_view_category_info_page import BusinessViewCategoryInfoPage
from .business_view_category_type import BusinessViewCategoryType
from .business_view_group_info import BusinessViewGroupInfo
from .business_view_group_info_page import BusinessViewGroupInfoPage
from .business_view_group_type import BusinessViewGroupType
from .capacity_tier_extent_info import CapacityTierExtentInfo
from .capacity_tier_extent_info_page import CapacityTierExtentInfoPage
from .cdp_policy_info import CdpPolicyInfo
from .cdp_policy_info_page import CdpPolicyInfoPage
from .cdp_policy_status import CdpPolicyStatus
from .certificate_advanced_info import CertificateAdvancedInfo
from .certificate_export_type import CertificateExportType
from .certificate_full_info import CertificateFullInfo
from .certificate_full_info_page import CertificateFullInfoPage
from .certificate_issuer_info import CertificateIssuerInfo
from .child_alarm_status import ChildAlarmStatus
from .cloud_database_backup_type import CloudDatabaseBackupType
from .cloud_database_info import CloudDatabaseInfo
from .cloud_database_info_page import CloudDatabaseInfoPage
from .cloud_database_instance_type import CloudDatabaseInstanceType
from .cloud_database_policy_info import CloudDatabasePolicyInfo
from .cloud_database_policy_info_page import CloudDatabasePolicyInfoPage
from .cloud_director_backup_job_info import CloudDirectorBackupJobInfo
from .cloud_director_backup_job_info_page import CloudDirectorBackupJobInfoPage
from .cloud_director_connection_state import CloudDirectorConnectionState
from .cloud_director_datastore_info import CloudDirectorDatastoreInfo
from .cloud_director_datastore_info_page import CloudDirectorDatastoreInfoPage
from .cloud_director_info import CloudDirectorInfo
from .cloud_director_info_page import CloudDirectorInfoPage
from .cloud_director_object_relations_info import CloudDirectorObjectRelationsInfo
from .cloud_director_object_relations_info_page import CloudDirectorObjectRelationsInfoPage
from .cloud_director_object_type import CloudDirectorObjectType
from .cloud_director_replication_job_info import CloudDirectorReplicationJobInfo
from .cloud_director_replication_job_info_page import CloudDirectorReplicationJobInfoPage
from .cloud_director_v_app_info import CloudDirectorVAppInfo
from .cloud_director_v_app_info_page import CloudDirectorVAppInfoPage
from .cloud_director_vm_info import CloudDirectorVmInfo
from .cloud_director_vm_info_page import CloudDirectorVmInfoPage
from .cloud_file_share_backup_type import CloudFileShareBackupType
from .cloud_file_share_info import CloudFileShareInfo
from .cloud_file_share_info_page import CloudFileShareInfoPage
from .cloud_file_share_instance_type import CloudFileShareInstanceType
from .cloud_file_share_policy_info import CloudFileSharePolicyInfo
from .cloud_file_share_policy_info_page import CloudFileSharePolicyInfoPage
from .cloud_file_shares_platform import CloudFileSharesPlatform
from .cloud_gateway_info import CloudGatewayInfo
from .cloud_gateway_info_page import CloudGatewayInfoPage
from .cloud_gateway_pool_info import CloudGatewayPoolInfo
from .cloud_gateway_pool_info_page import CloudGatewayPoolInfoPage
from .cloud_gateway_state import CloudGatewayState
from .cloud_instance import CloudInstance
from .cloud_network_instance_type import CloudNetworkInstanceType
from .cloud_network_policy_info import CloudNetworkPolicyInfo
from .cloud_network_policy_info_page import CloudNetworkPolicyInfoPage
from .cloud_networks_platform import CloudNetworksPlatform
from .cloud_platform import CloudPlatform
from .cloud_vm_backup_type import CloudVmBackupType
from .cloud_vm_info import CloudVmInfo
from .cloud_vm_info_page import CloudVmInfoPage
from .cloud_vm_instance_type import CloudVmInstanceType
from .cloud_vm_policy_info import CloudVmPolicyInfo
from .cloud_vm_policy_info_page import CloudVmPolicyInfoPage
from .collecting_object_type import CollectingObjectType
from .collecting_session_info import CollectingSessionInfo
from .collecting_session_info_page import CollectingSessionInfoPage
from .collecting_status import CollectingStatus
from .computer_operation_mode import ComputerOperationMode
from .computer_platform import ComputerPlatform
from .credential_assign_guest_request import CredentialAssignGuestRequest
from .credential_assign_host_request import CredentialAssignHostRequest
from .credential_info import CredentialInfo
from .credential_info_page import CredentialInfoPage
from .credential_save_request import CredentialSaveRequest
from .credentials_type import CredentialsType
from .datastore_connection_state import DatastoreConnectionState
from .day_of_week import DayOfWeek
from .day_of_week_appearance import DayOfWeekAppearance
from .enterprise_manager_connection_state import EnterpriseManagerConnectionState
from .enterprise_manager_server_info import EnterpriseManagerServerInfo
from .enterprise_manager_server_info_page import EnterpriseManagerServerInfoPage
from .entity_credentials_info import EntityCredentialsInfo
from .extent_repository_type import ExtentRepositoryType
from .external_repository_info import ExternalRepositoryInfo
from .external_repository_info_page import ExternalRepositoryInfoPage
from .external_repository_type import ExternalRepositoryType
from .failover_plan_info import FailoverPlanInfo
from .failover_plan_info_page import FailoverPlanInfoPage
from .failover_plan_state import FailoverPlanState
from .file_backup_job_info import FileBackupJobInfo
from .file_backup_job_info_page import FileBackupJobInfoPage
from .file_copy_job_info import FileCopyJobInfo
from .file_copy_job_info_page import FileCopyJobInfoPage
from .file_share_backup_job_type import FileShareBackupJobType
from .file_share_type import FileShareType
from .file_to_tape_job_info import FileToTapeJobInfo
from .file_to_tape_job_info_page import FileToTapeJobInfoPage
from .guest_assign_info import GuestAssignInfo
from .guest_assign_info_credential_assign_info import GuestAssignInfoCredentialAssignInfo
from .guest_assign_type import GuestAssignType
from .guest_settings_info import GuestSettingsInfo
from .guest_settings_request import GuestSettingsRequest
from .hardware_plan import HardwarePlan
from .host_assign_info import HostAssignInfo
from .host_assign_info_credential_assign_info import HostAssignInfoCredentialAssignInfo
from .host_assign_type import HostAssignType
from .hyper_v_cluster_info import HyperVClusterInfo
from .hyper_v_cluster_info_page import HyperVClusterInfoPage
from .hyper_v_connection_state import HyperVConnectionState
from .hyper_v_csv_info import HyperVCsvInfo
from .hyper_v_csv_info_page import HyperVCsvInfoPage
from .hyper_v_file_server_info import HyperVFileServerInfo
from .hyper_v_file_server_info_page import HyperVFileServerInfoPage
from .hyper_v_file_share_info import HyperVFileShareInfo
from .hyper_v_file_share_info_page import HyperVFileShareInfoPage
from .hyper_v_host_group_info import HyperVHostGroupInfo
from .hyper_v_host_group_info_page import HyperVHostGroupInfoPage
from .hyper_v_host_info import HyperVHostInfo
from .hyper_v_host_info_page import HyperVHostInfoPage
from .hyper_v_host_power_state import HyperVHostPowerState
from .hyper_v_integration_service import HyperVIntegrationService
from .hyper_v_object_relations_info import HyperVObjectRelationsInfo
from .hyper_v_object_relations_info_page import HyperVObjectRelationsInfoPage
from .hyper_v_object_type import HyperVObjectType
from .hyper_v_physical_disk_info import HyperVPhysicalDiskInfo
from .hyper_v_physical_disk_info_page import HyperVPhysicalDiskInfoPage
from .hyper_v_sc_vmm_server_info import HyperVScVmmServerInfo
from .hyper_v_sc_vmm_server_info_page import HyperVScVmmServerInfoPage
from .hyper_v_vm_info import HyperVVmInfo
from .hyper_v_vm_info_page import HyperVVmInfoPage
from .hyper_v_vm_power_state import HyperVVmPowerState
from .infrequent_access import InfrequentAccess
from .install_veeam_one_license_request import InstallVeeamOneLicenseRequest
from .job import Job
from .job_session_details_info import JobSessionDetailsInfo
from .job_session_details_info_page import JobSessionDetailsInfoPage
from .job_session_info import JobSessionInfo
from .job_session_info_page import JobSessionInfoPage
from .license_usage_report_status import LicenseUsageReportStatus
from .memory_shares_level import MemorySharesLevel
from .month import Month
from .object_storage_backup_job_info import ObjectStorageBackupJobInfo
from .object_storage_backup_job_info_page import ObjectStorageBackupJobInfoPage
from .object_storage_backup_job_type import ObjectStorageBackupJobType
from .object_storage_info import ObjectStorageInfo
from .object_storage_info_page import ObjectStorageInfoPage
from .object_storage_type import ObjectStorageType
from .object_to_tape_job_info import ObjectToTapeJobInfo
from .object_to_tape_job_info_page import ObjectToTapeJobInfoPage
from .organization_info import OrganizationInfo
from .organization_info_page import OrganizationInfoPage
from .organization_vdc_allocation_model import OrganizationVdcAllocationModel
from .organization_vdc_info import OrganizationVdcInfo
from .organization_vdc_info_page import OrganizationVdcInfoPage
from .organization_vdc_network_pool import OrganizationVdcNetworkPool
from .performance_tier_extent_info import PerformanceTierExtentInfo
from .performance_tier_extent_info_page import PerformanceTierExtentInfoPage
from .policy_state import PolicyState
from .problem_details import ProblemDetails
from .protected_application_info import ProtectedApplicationInfo
from .protected_application_info_page import ProtectedApplicationInfoPage
from .protected_application_platform import ProtectedApplicationPlatform
from .protected_cloud_database_backup_info import ProtectedCloudDatabaseBackupInfo
from .protected_cloud_database_backup_info_page import ProtectedCloudDatabaseBackupInfoPage
from .protected_cloud_database_info import ProtectedCloudDatabaseInfo
from .protected_cloud_database_info_page import ProtectedCloudDatabaseInfoPage
from .protected_cloud_database_restore_point_info import ProtectedCloudDatabaseRestorePointInfo
from .protected_cloud_database_restore_point_info_page import ProtectedCloudDatabaseRestorePointInfoPage
from .protected_cloud_file_share_backup_info import ProtectedCloudFileShareBackupInfo
from .protected_cloud_file_share_backup_info_page import ProtectedCloudFileShareBackupInfoPage
from .protected_cloud_file_share_info import ProtectedCloudFileShareInfo
from .protected_cloud_file_share_info_page import ProtectedCloudFileShareInfoPage
from .protected_cloud_file_share_restore_point_info import ProtectedCloudFileShareRestorePointInfo
from .protected_cloud_file_share_restore_point_info_page import ProtectedCloudFileShareRestorePointInfoPage
from .protected_cloud_network_backup_info import ProtectedCloudNetworkBackupInfo
from .protected_cloud_network_backup_info_page import ProtectedCloudNetworkBackupInfoPage
from .protected_cloud_network_info import ProtectedCloudNetworkInfo
from .protected_cloud_network_info_page import ProtectedCloudNetworkInfoPage
from .protected_cloud_network_restore_point_info import ProtectedCloudNetworkRestorePointInfo
from .protected_cloud_network_restore_point_info_page import ProtectedCloudNetworkRestorePointInfoPage
from .protected_cloud_vm_backup_info import ProtectedCloudVmBackupInfo
from .protected_cloud_vm_backup_info_page import ProtectedCloudVmBackupInfoPage
from .protected_cloud_vm_info import ProtectedCloudVmInfo
from .protected_cloud_vm_info_page import ProtectedCloudVmInfoPage
from .protected_cloud_vm_restore_point_info import ProtectedCloudVmRestorePointInfo
from .protected_cloud_vm_restore_point_info_page import ProtectedCloudVmRestorePointInfoPage
from .protected_computer_backup_info import ProtectedComputerBackupInfo
from .protected_computer_backup_info_page import ProtectedComputerBackupInfoPage
from .protected_computer_backup_restore_point_info import ProtectedComputerBackupRestorePointInfo
from .protected_computer_backup_restore_point_info_page import ProtectedComputerBackupRestorePointInfoPage
from .protected_computer_info import ProtectedComputerInfo
from .protected_computer_info_page import ProtectedComputerInfoPage
from .protected_computer_operation_mode import ProtectedComputerOperationMode
from .protected_computer_platform import ProtectedComputerPlatform
from .protected_data_repository_info import ProtectedDataRepositoryInfo
from .protected_database_backup_info import ProtectedDatabaseBackupInfo
from .protected_database_backup_info_page import ProtectedDatabaseBackupInfoPage
from .protected_file_share_backup_info import ProtectedFileShareBackupInfo
from .protected_file_share_backup_info_page import ProtectedFileShareBackupInfoPage
from .protected_file_share_backup_restore_point_info import ProtectedFileShareBackupRestorePointInfo
from .protected_file_share_backup_restore_point_info_page import ProtectedFileShareBackupRestorePointInfoPage
from .protected_file_share_info import ProtectedFileShareInfo
from .protected_file_share_info_page import ProtectedFileShareInfoPage
from .protected_object_storage_backup_info import ProtectedObjectStorageBackupInfo
from .protected_object_storage_backup_info_page import ProtectedObjectStorageBackupInfoPage
from .protected_object_storage_backup_restore_point_info import ProtectedObjectStorageBackupRestorePointInfo
from .protected_object_storage_backup_restore_point_info_page import ProtectedObjectStorageBackupRestorePointInfoPage
from .protected_object_storage_info import ProtectedObjectStorageInfo
from .protected_object_storage_info_page import ProtectedObjectStorageInfoPage
from .protected_object_storage_type import ProtectedObjectStorageType
from .protected_vm_backup_info import ProtectedVmBackupInfo
from .protected_vm_backup_info_page import ProtectedVmBackupInfoPage
from .protected_vm_backup_restore_point_info import ProtectedVmBackupRestorePointInfo
from .protected_vm_backup_restore_point_info_page import ProtectedVmBackupRestorePointInfoPage
from .protected_vm_info import ProtectedVmInfo
from .protected_vm_info_page import ProtectedVmInfoPage
from .protected_vm_replica_restore_point_info import ProtectedVmReplicaRestorePointInfo
from .protected_vm_replica_restore_point_info_page import ProtectedVmReplicaRestorePointInfoPage
from .protection_group import ProtectionGroup
from .provider_vdc import ProviderVdc
from .provider_vdc_info import ProviderVdcInfo
from .provider_vdc_info_page import ProviderVdcInfoPage
from .regular_repository_type import RegularRepositoryType
from .remediation import Remediation
from .remediation_mode import RemediationMode
from .remediations import Remediations
from .repository_state import RepositoryState
from .resolve_multiple_triggered_alarms_request import ResolveMultipleTriggeredAlarmsRequest
from .resolve_multiple_triggered_child_alarms_request import ResolveMultipleTriggeredChildAlarmsRequest
from .resolve_type import ResolveType
from .scaleout_repository_info import ScaleoutRepositoryInfo
from .scaleout_repository_info_page import ScaleoutRepositoryInfoPage
from .scaleout_repository_policy import ScaleoutRepositoryPolicy
from .schedule_interval_type import ScheduleIntervalType
from .schedule_plan import SchedulePlan
from .schedule_plan_daily import SchedulePlanDaily
from .schedule_plan_monthly_days import SchedulePlanMonthlyDays
from .schedule_plan_monthly_week_days import SchedulePlanMonthlyWeekDays
from .schedule_plan_periodical import SchedulePlanPeriodical
from .schedule_session_status import ScheduleSessionStatus
from .schedule_type import ScheduleType
from .server_information import ServerInformation
from .sessions_task_types import SessionsTaskTypes
from .sure_backup_job_info import SureBackupJobInfo
from .sure_backup_job_info_page import SureBackupJobInfoPage
from .tape_server_info import TapeServerInfo
from .tape_server_info_page import TapeServerInfoPage
from .tenant_info import TenantInfo
from .tenant_info_page import TenantInfoPage
from .tenant_quotas_info import TenantQuotasInfo
from .tenant_quotas_info_page import TenantQuotasInfoPage
from .tenant_type import TenantType
from .token_response import TokenResponse
from .transaction_log_backup_job_info import TransactionLogBackupJobInfo
from .transaction_log_backup_job_info_page import TransactionLogBackupJobInfoPage
from .transaction_log_backup_job_type import TransactionLogBackupJobType
from .transaction_log_backup_parent_job import TransactionLogBackupParentJob
from .transaction_log_backup_parent_job_type import TransactionLogBackupParentJobType
from .triggered_alarm_info_2 import TriggeredAlarmInfo2
from .triggered_alarm_info_2_page import TriggeredAlarmInfo2Page
from .triggered_child_alarm_info import TriggeredChildAlarmInfo
from .triggered_child_alarm_info_page import TriggeredChildAlarmInfoPage
from .unstructured_data_source import UnstructuredDataSource
from .updater_info import UpdaterInfo
from .v_app_power_state import VAppPowerState
from .v_center_connection_state import VCenterConnectionState
from .v_center_server_info import VCenterServerInfo
from .v_center_server_info_page import VCenterServerInfoPage
from .v_sphere_datastore_cluster_info import VSphereDatastoreClusterInfo
from .v_sphere_datastore_cluster_info_page import VSphereDatastoreClusterInfoPage
from .v_sphere_datastore_info import VSphereDatastoreInfo
from .v_sphere_datastore_info_page import VSphereDatastoreInfoPage
from .v_sphere_datastore_type import VSphereDatastoreType
from .v_sphere_drs_automation_level import VSphereDrsAutomationLevel
from .v_sphere_host_and_cluster_folder_info import VSphereHostAndClusterFolderInfo
from .v_sphere_host_and_cluster_folder_info_page import VSphereHostAndClusterFolderInfoPage
from .v_sphere_host_cluster_info import VSphereHostClusterInfo
from .v_sphere_host_cluster_info_page import VSphereHostClusterInfoPage
from .v_sphere_host_connection_state import VSphereHostConnectionState
from .v_sphere_host_info import VSphereHostInfo
from .v_sphere_host_info_page import VSphereHostInfoPage
from .v_sphere_host_power_state import VSphereHostPowerState
from .v_sphere_host_sensor_info import VSphereHostSensorInfo
from .v_sphere_host_sensor_info_page import VSphereHostSensorInfoPage
from .v_sphere_host_sensor_state import VSphereHostSensorState
from .v_sphere_object_relations_info import VSphereObjectRelationsInfo
from .v_sphere_object_relations_info_page import VSphereObjectRelationsInfoPage
from .v_sphere_object_type import VSphereObjectType
from .v_sphere_resource_pool_info import VSphereResourcePoolInfo
from .v_sphere_resource_pool_info_page import VSphereResourcePoolInfoPage
from .v_sphere_v_app_info import VSphereVAppInfo
from .v_sphere_v_app_info_page import VSphereVAppInfoPage
from .v_sphere_vm_connection_state import VSphereVmConnectionState
from .v_sphere_vm_info import VSphereVmInfo
from .v_sphere_vm_info_page import VSphereVmInfoPage
from .v_sphere_vm_power_state import VSphereVmPowerState
from .vb_365_aws_region_type import Vb365AwsRegionType
from .vb_365_backup_job import Vb365BackupJob
from .vb_365_backup_job_page import Vb365BackupJobPage
from .vb_365_backup_proxy_info import Vb365BackupProxyInfo
from .vb_365_backup_proxy_info_page import Vb365BackupProxyInfoPage
from .vb_365_backup_proxy_pool_info import Vb365BackupProxyPoolInfo
from .vb_365_backup_proxy_pool_info_page import Vb365BackupProxyPoolInfoPage
from .vb_365_backup_repository_info import Vb365BackupRepositoryInfo
from .vb_365_backup_repository_info_page import Vb365BackupRepositoryInfoPage
from .vb_365_backup_repository_object_storage_type import Vb365BackupRepositoryObjectStorageType
from .vb_365_backup_repository_retention_daily_type import Vb365BackupRepositoryRetentionDailyType
from .vb_365_backup_repository_retention_frequency_type import Vb365BackupRepositoryRetentionFrequencyType
from .vb_365_backup_repository_retention_period_type import Vb365BackupRepositoryRetentionPeriodType
from .vb_365_backup_repository_retention_type import Vb365BackupRepositoryRetentionType
from .vb_365_backup_repository_retention_yearly_period_type import Vb365BackupRepositoryRetentionYearlyPeriodType
from .vb_365_backup_type import Vb365BackupType
from .vb_365_copy_job import Vb365CopyJob
from .vb_365_copy_job_page import Vb365CopyJobPage
from .vb_365_copy_job_schedule_type import Vb365CopyJobScheduleType
from .vb_365_day_of_week import Vb365DayOfWeek
from .vb_365_group_info import Vb365GroupInfo
from .vb_365_group_info_page import Vb365GroupInfoPage
from .vb_365_group_location_type import Vb365GroupLocationType
from .vb_365_group_type import Vb365GroupType
from .vb_365_internet_proxy_type import Vb365InternetProxyType
from .vb_365_job_status import Vb365JobStatus
from .vb_365_job_type import Vb365JobType
from .vb_365_monthly_day_number import Vb365MonthlyDayNumber
from .vb_365_object_relations_info import Vb365ObjectRelationsInfo
from .vb_365_object_relations_info_page import Vb365ObjectRelationsInfoPage
from .vb_365_object_storage_repository_info import Vb365ObjectStorageRepositoryInfo
from .vb_365_object_storage_repository_info_page import Vb365ObjectStorageRepositoryInfoPage
from .vb_365_object_storage_repository_type import Vb365ObjectStorageRepositoryType
from .vb_365_object_type import Vb365ObjectType
from .vb_365_organization_info import Vb365OrganizationInfo
from .vb_365_organization_info_page import Vb365OrganizationInfoPage
from .vb_365_organization_region import Vb365OrganizationRegion
from .vb_365_organization_type import Vb365OrganizationType
from .vb_365_protected_group_info import Vb365ProtectedGroupInfo
from .vb_365_protected_group_info_page import Vb365ProtectedGroupInfoPage
from .vb_365_protected_group_restore_point_info import Vb365ProtectedGroupRestorePointInfo
from .vb_365_protected_group_restore_point_info_i_page import Vb365ProtectedGroupRestorePointInfoIPage
from .vb_365_protected_group_restore_point_info_page import Vb365ProtectedGroupRestorePointInfoPage
from .vb_365_protected_site_info import Vb365ProtectedSiteInfo
from .vb_365_protected_site_info_page import Vb365ProtectedSiteInfoPage
from .vb_365_protected_site_restore_point_info import Vb365ProtectedSiteRestorePointInfo
from .vb_365_protected_site_restore_point_info_page import Vb365ProtectedSiteRestorePointInfoPage
from .vb_365_protected_team_info import Vb365ProtectedTeamInfo
from .vb_365_protected_team_info_page import Vb365ProtectedTeamInfoPage
from .vb_365_protected_team_restore_point_info import Vb365ProtectedTeamRestorePointInfo
from .vb_365_protected_team_restore_point_info_page import Vb365ProtectedTeamRestorePointInfoPage
from .vb_365_protected_user_info import Vb365ProtectedUserInfo
from .vb_365_protected_user_info_page import Vb365ProtectedUserInfoPage
from .vb_365_protected_user_restore_point_info import Vb365ProtectedUserRestorePointInfo
from .vb_365_protected_user_restore_point_info_page import Vb365ProtectedUserRestorePointInfoPage
from .vb_365_proxy_status import Vb365ProxyStatus
from .vb_365_proxy_type import Vb365ProxyType
from .vb_365_server_connection_state import Vb365ServerConnectionState
from .vb_365_server_info import Vb365ServerInfo
from .vb_365_server_info_page import Vb365ServerInfoPage
from .vb_365_site_info import Vb365SiteInfo
from .vb_365_site_info_page import Vb365SiteInfoPage
from .vb_365_team_info import Vb365TeamInfo
from .vb_365_team_info_page import Vb365TeamInfoPage
from .vb_365_user_info import Vb365UserInfo
from .vb_365_user_info_page import Vb365UserInfoPage
from .vb_365_user_type import Vb365UserType
from .vbr_object_relations_info import VbrObjectRelationsInfo
from .vbr_object_relations_info_page import VbrObjectRelationsInfoPage
from .vbr_object_type import VbrObjectType
from .veeam_one_license_info import VeeamOneLicenseInfo
from .veeam_one_license_settings import VeeamOneLicenseSettings
from .veeam_one_license_type import VeeamOneLicenseType
from .veeam_one_license_usage_common_workload import VeeamOneLicenseUsageCommonWorkload
from .veeam_one_license_usage_current import VeeamOneLicenseUsageCurrent
from .veeam_one_license_usage_report import VeeamOneLicenseUsageReport
from .veeam_one_license_usage_report_approve import VeeamOneLicenseUsageReportApprove
from .veeam_one_license_usage_report_approve_workload import VeeamOneLicenseUsageReportApproveWorkload
from .veeam_one_license_usage_report_workload import VeeamOneLicenseUsageReportWorkload
from .veeam_one_license_usage_total import VeeamOneLicenseUsageTotal
from .veeam_one_license_usage_total_unit import VeeamOneLicenseUsageTotalUnit
from .veeam_one_license_usage_unit_type import VeeamOneLicenseUsageUnitType
from .veeam_one_logs_request import VeeamOneLogsRequest
from .veeam_one_service_info import VeeamOneServiceInfo
from .vm_backup_job_info import VmBackupJobInfo
from .vm_backup_job_info_page import VmBackupJobInfoPage
from .vm_backup_job_platform import VmBackupJobPlatform
from .vm_backup_type import VmBackupType
from .vm_copy_job_info import VmCopyJobInfo
from .vm_copy_job_info_page import VmCopyJobInfoPage
from .vm_datastore_usage import VmDatastoreUsage
from .vm_guest_disk import VmGuestDisk
from .vm_platform import VmPlatform
from .vm_replication_job_info import VmReplicationJobInfo
from .vm_replication_job_info_page import VmReplicationJobInfoPage
from .vm_replication_job_platform import VmReplicationJobPlatform
from .vm_snapshot_only_job_info import VmSnapshotOnlyJobInfo
from .vm_snapshot_only_job_info_page import VmSnapshotOnlyJobInfoPage
from .vm_virtual_disk import VmVirtualDisk
from .wan_accelerator_info import WanAcceleratorInfo
from .wan_accelerator_info_page import WanAcceleratorInfoPage
from .wan_accelerator_state import WanAcceleratorState

__all__ = (
    "AccessTokenRole",
    "AgentBackupJobInfo",
    "AgentBackupJobInfoPage",
    "AgentBackupJobPlatform",
    "AgentBackupJobType",
    "AgentPolicyChildJobInfo",
    "AgentPolicyChildJobInfoPage",
    "AgentPolicyInfo",
    "AgentPolicyInfoPage",
    "AlarmAssignment",
    "AlarmAssignmentObjectType",
    "AlarmSource",
    "AlarmSourceObjectType",
    "AlarmStatus",
    "AlarmTemplateInfo",
    "AlarmTemplateInfoPage",
    "AlarmTemplateType",
    "ApplicationBackupJobInfo",
    "ApplicationBackupJobInfoPage",
    "ApplicationBackupJobStatus",
    "ApplicationInfo",
    "ApplicationInfoPage",
    "ApplicationJobPlatform",
    "ApplicationPlatform",
    "ApplicationTransactionLogBackupJobInfo",
    "ApplicationTransactionLogBackupJobInfoPage",
    "ArchiveTierExtentInfo",
    "ArchiveTierExtentInfoPage",
    "AssignType",
    "AsyncTaskState",
    "AsyncTaskStatus",
    "AuthenticationCreateTokenDataBody",
    "AuthenticationCreateTokenDataBodyGrantType",
    "AuthenticationCreateTokenFilesBody",
    "AuthenticationCreateTokenFilesBodyGrantType",
    "AuthenticationRevokeTokenDataBody",
    "AuthenticationRevokeTokenFilesBody",
    "BackupAgentInfo",
    "BackupAgentInfoPage",
    "BackupAgentStatus",
    "BackupClusterInfo",
    "BackupClusterInfoPage",
    "BackupCopyChildJobInfo",
    "BackupCopyChildJobInfoPage",
    "BackupCopyJobInfo",
    "BackupCopyJobInfoPage",
    "BackupJobStatus",
    "BackupPlatformType",
    "BackupProxyInfo",
    "BackupProxyInfoPage",
    "BackupProxyState",
    "BackupProxyTransportMode",
    "BackupProxyType",
    "BackupRepositoryInfo",
    "BackupRepositoryInfoPage",
    "BackupRepositoryType",
    "BackupServerConnectionState",
    "BackupServerInfo",
    "BackupServerInfoPage",
    "BackupToTapeJobInfo",
    "BackupToTapeJobInfoPage",
    "BestPracticeCheckStatus",
    "BestPracticeGroup",
    "BestPracticeInfo",
    "BestPracticeInfoPage",
    "BestPracticeStatus",
    "BusinessViewCategoryInfo",
    "BusinessViewCategoryInfoPage",
    "BusinessViewCategoryType",
    "BusinessViewGroupInfo",
    "BusinessViewGroupInfoPage",
    "BusinessViewGroupType",
    "CapacityTierExtentInfo",
    "CapacityTierExtentInfoPage",
    "CdpPolicyInfo",
    "CdpPolicyInfoPage",
    "CdpPolicyStatus",
    "CertificateAdvancedInfo",
    "CertificateExportType",
    "CertificateFullInfo",
    "CertificateFullInfoPage",
    "CertificateIssuerInfo",
    "ChildAlarmStatus",
    "CloudDatabaseBackupType",
    "CloudDatabaseInfo",
    "CloudDatabaseInfoPage",
    "CloudDatabaseInstanceType",
    "CloudDatabasePolicyInfo",
    "CloudDatabasePolicyInfoPage",
    "CloudDirectorBackupJobInfo",
    "CloudDirectorBackupJobInfoPage",
    "CloudDirectorConnectionState",
    "CloudDirectorDatastoreInfo",
    "CloudDirectorDatastoreInfoPage",
    "CloudDirectorInfo",
    "CloudDirectorInfoPage",
    "CloudDirectorObjectRelationsInfo",
    "CloudDirectorObjectRelationsInfoPage",
    "CloudDirectorObjectType",
    "CloudDirectorReplicationJobInfo",
    "CloudDirectorReplicationJobInfoPage",
    "CloudDirectorVAppInfo",
    "CloudDirectorVAppInfoPage",
    "CloudDirectorVmInfo",
    "CloudDirectorVmInfoPage",
    "CloudFileShareBackupType",
    "CloudFileShareInfo",
    "CloudFileShareInfoPage",
    "CloudFileShareInstanceType",
    "CloudFileSharePolicyInfo",
    "CloudFileSharePolicyInfoPage",
    "CloudFileSharesPlatform",
    "CloudGatewayInfo",
    "CloudGatewayInfoPage",
    "CloudGatewayPoolInfo",
    "CloudGatewayPoolInfoPage",
    "CloudGatewayState",
    "CloudInstance",
    "CloudNetworkInstanceType",
    "CloudNetworkPolicyInfo",
    "CloudNetworkPolicyInfoPage",
    "CloudNetworksPlatform",
    "CloudPlatform",
    "CloudVmBackupType",
    "CloudVmInfo",
    "CloudVmInfoPage",
    "CloudVmInstanceType",
    "CloudVmPolicyInfo",
    "CloudVmPolicyInfoPage",
    "CollectingObjectType",
    "CollectingSessionInfo",
    "CollectingSessionInfoPage",
    "CollectingStatus",
    "ComputerOperationMode",
    "ComputerPlatform",
    "CredentialAssignGuestRequest",
    "CredentialAssignHostRequest",
    "CredentialInfo",
    "CredentialInfoPage",
    "CredentialSaveRequest",
    "CredentialsType",
    "DatastoreConnectionState",
    "DayOfWeek",
    "DayOfWeekAppearance",
    "EnterpriseManagerConnectionState",
    "EnterpriseManagerServerInfo",
    "EnterpriseManagerServerInfoPage",
    "EntityCredentialsInfo",
    "ExtentRepositoryType",
    "ExternalRepositoryInfo",
    "ExternalRepositoryInfoPage",
    "ExternalRepositoryType",
    "FailoverPlanInfo",
    "FailoverPlanInfoPage",
    "FailoverPlanState",
    "FileBackupJobInfo",
    "FileBackupJobInfoPage",
    "FileCopyJobInfo",
    "FileCopyJobInfoPage",
    "FileShareBackupJobType",
    "FileShareType",
    "FileToTapeJobInfo",
    "FileToTapeJobInfoPage",
    "GuestAssignInfo",
    "GuestAssignInfoCredentialAssignInfo",
    "GuestAssignType",
    "GuestSettingsInfo",
    "GuestSettingsRequest",
    "HardwarePlan",
    "HostAssignInfo",
    "HostAssignInfoCredentialAssignInfo",
    "HostAssignType",
    "HyperVClusterInfo",
    "HyperVClusterInfoPage",
    "HyperVConnectionState",
    "HyperVCsvInfo",
    "HyperVCsvInfoPage",
    "HyperVFileServerInfo",
    "HyperVFileServerInfoPage",
    "HyperVFileShareInfo",
    "HyperVFileShareInfoPage",
    "HyperVHostGroupInfo",
    "HyperVHostGroupInfoPage",
    "HyperVHostInfo",
    "HyperVHostInfoPage",
    "HyperVHostPowerState",
    "HyperVIntegrationService",
    "HyperVObjectRelationsInfo",
    "HyperVObjectRelationsInfoPage",
    "HyperVObjectType",
    "HyperVPhysicalDiskInfo",
    "HyperVPhysicalDiskInfoPage",
    "HyperVScVmmServerInfo",
    "HyperVScVmmServerInfoPage",
    "HyperVVmInfo",
    "HyperVVmInfoPage",
    "HyperVVmPowerState",
    "InfrequentAccess",
    "InstallVeeamOneLicenseRequest",
    "Job",
    "JobSessionDetailsInfo",
    "JobSessionDetailsInfoPage",
    "JobSessionInfo",
    "JobSessionInfoPage",
    "LicenseUsageReportStatus",
    "MemorySharesLevel",
    "Month",
    "ObjectStorageBackupJobInfo",
    "ObjectStorageBackupJobInfoPage",
    "ObjectStorageBackupJobType",
    "ObjectStorageInfo",
    "ObjectStorageInfoPage",
    "ObjectStorageType",
    "ObjectToTapeJobInfo",
    "ObjectToTapeJobInfoPage",
    "OrganizationInfo",
    "OrganizationInfoPage",
    "OrganizationVdcAllocationModel",
    "OrganizationVdcInfo",
    "OrganizationVdcInfoPage",
    "OrganizationVdcNetworkPool",
    "PerformanceTierExtentInfo",
    "PerformanceTierExtentInfoPage",
    "PolicyState",
    "ProblemDetails",
    "ProtectedApplicationInfo",
    "ProtectedApplicationInfoPage",
    "ProtectedApplicationPlatform",
    "ProtectedCloudDatabaseBackupInfo",
    "ProtectedCloudDatabaseBackupInfoPage",
    "ProtectedCloudDatabaseInfo",
    "ProtectedCloudDatabaseInfoPage",
    "ProtectedCloudDatabaseRestorePointInfo",
    "ProtectedCloudDatabaseRestorePointInfoPage",
    "ProtectedCloudFileShareBackupInfo",
    "ProtectedCloudFileShareBackupInfoPage",
    "ProtectedCloudFileShareInfo",
    "ProtectedCloudFileShareInfoPage",
    "ProtectedCloudFileShareRestorePointInfo",
    "ProtectedCloudFileShareRestorePointInfoPage",
    "ProtectedCloudNetworkBackupInfo",
    "ProtectedCloudNetworkBackupInfoPage",
    "ProtectedCloudNetworkInfo",
    "ProtectedCloudNetworkInfoPage",
    "ProtectedCloudNetworkRestorePointInfo",
    "ProtectedCloudNetworkRestorePointInfoPage",
    "ProtectedCloudVmBackupInfo",
    "ProtectedCloudVmBackupInfoPage",
    "ProtectedCloudVmInfo",
    "ProtectedCloudVmInfoPage",
    "ProtectedCloudVmRestorePointInfo",
    "ProtectedCloudVmRestorePointInfoPage",
    "ProtectedComputerBackupInfo",
    "ProtectedComputerBackupInfoPage",
    "ProtectedComputerBackupRestorePointInfo",
    "ProtectedComputerBackupRestorePointInfoPage",
    "ProtectedComputerInfo",
    "ProtectedComputerInfoPage",
    "ProtectedComputerOperationMode",
    "ProtectedComputerPlatform",
    "ProtectedDatabaseBackupInfo",
    "ProtectedDatabaseBackupInfoPage",
    "ProtectedDataRepositoryInfo",
    "ProtectedFileShareBackupInfo",
    "ProtectedFileShareBackupInfoPage",
    "ProtectedFileShareBackupRestorePointInfo",
    "ProtectedFileShareBackupRestorePointInfoPage",
    "ProtectedFileShareInfo",
    "ProtectedFileShareInfoPage",
    "ProtectedObjectStorageBackupInfo",
    "ProtectedObjectStorageBackupInfoPage",
    "ProtectedObjectStorageBackupRestorePointInfo",
    "ProtectedObjectStorageBackupRestorePointInfoPage",
    "ProtectedObjectStorageInfo",
    "ProtectedObjectStorageInfoPage",
    "ProtectedObjectStorageType",
    "ProtectedVmBackupInfo",
    "ProtectedVmBackupInfoPage",
    "ProtectedVmBackupRestorePointInfo",
    "ProtectedVmBackupRestorePointInfoPage",
    "ProtectedVmInfo",
    "ProtectedVmInfoPage",
    "ProtectedVmReplicaRestorePointInfo",
    "ProtectedVmReplicaRestorePointInfoPage",
    "ProtectionGroup",
    "ProviderVdc",
    "ProviderVdcInfo",
    "ProviderVdcInfoPage",
    "RegularRepositoryType",
    "Remediation",
    "RemediationMode",
    "Remediations",
    "RepositoryState",
    "ResolveMultipleTriggeredAlarmsRequest",
    "ResolveMultipleTriggeredChildAlarmsRequest",
    "ResolveType",
    "ScaleoutRepositoryInfo",
    "ScaleoutRepositoryInfoPage",
    "ScaleoutRepositoryPolicy",
    "ScheduleIntervalType",
    "SchedulePlan",
    "SchedulePlanDaily",
    "SchedulePlanMonthlyDays",
    "SchedulePlanMonthlyWeekDays",
    "SchedulePlanPeriodical",
    "ScheduleSessionStatus",
    "ScheduleType",
    "ServerInformation",
    "SessionsTaskTypes",
    "SureBackupJobInfo",
    "SureBackupJobInfoPage",
    "TapeServerInfo",
    "TapeServerInfoPage",
    "TenantInfo",
    "TenantInfoPage",
    "TenantQuotasInfo",
    "TenantQuotasInfoPage",
    "TenantType",
    "TokenResponse",
    "TransactionLogBackupJobInfo",
    "TransactionLogBackupJobInfoPage",
    "TransactionLogBackupJobType",
    "TransactionLogBackupParentJob",
    "TransactionLogBackupParentJobType",
    "TriggeredAlarmInfo2",
    "TriggeredAlarmInfo2Page",
    "TriggeredChildAlarmInfo",
    "TriggeredChildAlarmInfoPage",
    "UnstructuredDataSource",
    "UpdaterInfo",
    "VAppPowerState",
    "Vb365AwsRegionType",
    "Vb365BackupJob",
    "Vb365BackupJobPage",
    "Vb365BackupProxyInfo",
    "Vb365BackupProxyInfoPage",
    "Vb365BackupProxyPoolInfo",
    "Vb365BackupProxyPoolInfoPage",
    "Vb365BackupRepositoryInfo",
    "Vb365BackupRepositoryInfoPage",
    "Vb365BackupRepositoryObjectStorageType",
    "Vb365BackupRepositoryRetentionDailyType",
    "Vb365BackupRepositoryRetentionFrequencyType",
    "Vb365BackupRepositoryRetentionPeriodType",
    "Vb365BackupRepositoryRetentionType",
    "Vb365BackupRepositoryRetentionYearlyPeriodType",
    "Vb365BackupType",
    "Vb365CopyJob",
    "Vb365CopyJobPage",
    "Vb365CopyJobScheduleType",
    "Vb365DayOfWeek",
    "Vb365GroupInfo",
    "Vb365GroupInfoPage",
    "Vb365GroupLocationType",
    "Vb365GroupType",
    "Vb365InternetProxyType",
    "Vb365JobStatus",
    "Vb365JobType",
    "Vb365MonthlyDayNumber",
    "Vb365ObjectRelationsInfo",
    "Vb365ObjectRelationsInfoPage",
    "Vb365ObjectStorageRepositoryInfo",
    "Vb365ObjectStorageRepositoryInfoPage",
    "Vb365ObjectStorageRepositoryType",
    "Vb365ObjectType",
    "Vb365OrganizationInfo",
    "Vb365OrganizationInfoPage",
    "Vb365OrganizationRegion",
    "Vb365OrganizationType",
    "Vb365ProtectedGroupInfo",
    "Vb365ProtectedGroupInfoPage",
    "Vb365ProtectedGroupRestorePointInfo",
    "Vb365ProtectedGroupRestorePointInfoIPage",
    "Vb365ProtectedGroupRestorePointInfoPage",
    "Vb365ProtectedSiteInfo",
    "Vb365ProtectedSiteInfoPage",
    "Vb365ProtectedSiteRestorePointInfo",
    "Vb365ProtectedSiteRestorePointInfoPage",
    "Vb365ProtectedTeamInfo",
    "Vb365ProtectedTeamInfoPage",
    "Vb365ProtectedTeamRestorePointInfo",
    "Vb365ProtectedTeamRestorePointInfoPage",
    "Vb365ProtectedUserInfo",
    "Vb365ProtectedUserInfoPage",
    "Vb365ProtectedUserRestorePointInfo",
    "Vb365ProtectedUserRestorePointInfoPage",
    "Vb365ProxyStatus",
    "Vb365ProxyType",
    "Vb365ServerConnectionState",
    "Vb365ServerInfo",
    "Vb365ServerInfoPage",
    "Vb365SiteInfo",
    "Vb365SiteInfoPage",
    "Vb365TeamInfo",
    "Vb365TeamInfoPage",
    "Vb365UserInfo",
    "Vb365UserInfoPage",
    "Vb365UserType",
    "VbrObjectRelationsInfo",
    "VbrObjectRelationsInfoPage",
    "VbrObjectType",
    "VCenterConnectionState",
    "VCenterServerInfo",
    "VCenterServerInfoPage",
    "VeeamOneLicenseInfo",
    "VeeamOneLicenseSettings",
    "VeeamOneLicenseType",
    "VeeamOneLicenseUsageCommonWorkload",
    "VeeamOneLicenseUsageCurrent",
    "VeeamOneLicenseUsageReport",
    "VeeamOneLicenseUsageReportApprove",
    "VeeamOneLicenseUsageReportApproveWorkload",
    "VeeamOneLicenseUsageReportWorkload",
    "VeeamOneLicenseUsageTotal",
    "VeeamOneLicenseUsageTotalUnit",
    "VeeamOneLicenseUsageUnitType",
    "VeeamOneLogsRequest",
    "VeeamOneServiceInfo",
    "VmBackupJobInfo",
    "VmBackupJobInfoPage",
    "VmBackupJobPlatform",
    "VmBackupType",
    "VmCopyJobInfo",
    "VmCopyJobInfoPage",
    "VmDatastoreUsage",
    "VmGuestDisk",
    "VmPlatform",
    "VmReplicationJobInfo",
    "VmReplicationJobInfoPage",
    "VmReplicationJobPlatform",
    "VmSnapshotOnlyJobInfo",
    "VmSnapshotOnlyJobInfoPage",
    "VmVirtualDisk",
    "VSphereDatastoreClusterInfo",
    "VSphereDatastoreClusterInfoPage",
    "VSphereDatastoreInfo",
    "VSphereDatastoreInfoPage",
    "VSphereDatastoreType",
    "VSphereDrsAutomationLevel",
    "VSphereHostAndClusterFolderInfo",
    "VSphereHostAndClusterFolderInfoPage",
    "VSphereHostClusterInfo",
    "VSphereHostClusterInfoPage",
    "VSphereHostConnectionState",
    "VSphereHostInfo",
    "VSphereHostInfoPage",
    "VSphereHostPowerState",
    "VSphereHostSensorInfo",
    "VSphereHostSensorInfoPage",
    "VSphereHostSensorState",
    "VSphereObjectRelationsInfo",
    "VSphereObjectRelationsInfoPage",
    "VSphereObjectType",
    "VSphereResourcePoolInfo",
    "VSphereResourcePoolInfoPage",
    "VSphereVAppInfo",
    "VSphereVAppInfoPage",
    "VSphereVmConnectionState",
    "VSphereVmInfo",
    "VSphereVmInfoPage",
    "VSphereVmPowerState",
    "WanAcceleratorInfo",
    "WanAcceleratorInfoPage",
    "WanAcceleratorState",
)
