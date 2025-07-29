import pulumi
import requests
from typing import Dict, Any, Optional

class TableProvider(pulumi.dynamic.ResourceProvider):
    
    def create(self, inputs: Dict[str, Any]) -> pulumi.dynamic.CreateResult:
        name = inputs["name"]
        size = inputs["size"]
        read_only = inputs["read_only"]
        endpoint = inputs["endpoint"]
        
        payload = {
            "name": name,
            "size": int(size),  # Explicit int conversion
            "readOnly": read_only
        }
        
        try:
            response = requests.post(
                f"{endpoint}/table",
                headers={"Content-Type": "application/json"},
                json=payload,
                timeout=30
            )

            if response.status_code != 200:
                raise Exception(f"Failed to create table: {response.status_code} - {response.text}")

            result = response.json()

            return pulumi.dynamic.CreateResult(
                id_=str(result["id"]),
                outs={
                    "name": name,
                    "size": int(size),  # Ensure output is int
                    "read_only": read_only,
                    "endpoint": endpoint,
                    "created_at": result.get("createdAt", ""),
                    "modified_at": result.get("modifiedAt", "")
                }
            )
        except requests.exceptions.RequestException as e:
            raise Exception(f"Network error creating table: {str(e)}")

    def update(self, 
               id_: str, 
               old_inputs: Dict[str, Any], 
               new_inputs: Dict[str, Any]) -> pulumi.dynamic.UpdateResult:
        
        # Only call service if actual table properties changed
        if (old_inputs.get("name") != new_inputs.get("name") or 
            old_inputs.get("size") != new_inputs.get("size") or 
            old_inputs.get("read_only") != new_inputs.get("read_only")):
            
            payload = {
                "name": new_inputs["name"],
                "size": int(new_inputs["size"]),  # Explicit int conversion
                "readOnly": new_inputs["read_only"]
            }
            
            try:
                response = requests.patch(
                    f"{new_inputs['endpoint']}/table/{id_}",
                    headers={"Content-Type": "application/json"},
                    json=payload,
                    timeout=30
                )

                if response.status_code != 200:
                    raise Exception(f"Failed to update table: {response.status_code} - {response.text}")

                result = response.json()

                return pulumi.dynamic.UpdateResult(
                    outs={
                        "name": new_inputs["name"],
                        "size": int(new_inputs["size"]),  # Ensure output is int
                        "read_only": new_inputs["read_only"],
                        "endpoint": new_inputs["endpoint"],
                        "created_at": result.get("createdAt", old_inputs.get("created_at", "")),
                        "modified_at": result.get("modifiedAt", "")
                    }
                )
            except requests.exceptions.RequestException as e:
                raise Exception(f"Network error updating table: {str(e)}")
        else:
            # Only state changed, no service call needed
            return pulumi.dynamic.UpdateResult(
                outs={
                    "name": new_inputs["name"],
                    "size": int(new_inputs["size"]),  # Ensure output is int
                    "read_only": new_inputs["read_only"],
                    "endpoint": new_inputs["endpoint"],
                    "created_at": old_inputs.get("created_at", ""),
                    "modified_at": old_inputs.get("modified_at", "")
                }
            )

    def delete(self, id_: str, inputs: Dict[str, Any]) -> None:
        try:
            response = requests.delete(
                f"{inputs['endpoint']}/table/{id_}",
                timeout=30
            )

            if response.status_code != 200:
                raise Exception(f"Failed to delete table: {response.status_code} - {response.text}")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Network error deleting table: {str(e)}")

    def diff(self, 
             id_: str, 
             old_inputs: Dict[str, Any], 
             new_inputs: Dict[str, Any]) -> pulumi.dynamic.DiffResult:
        
        # Compare actual values
        name_changed = old_inputs.get("name", "").lower() != new_inputs.get("name", "").lower()
        size_changed = int(old_inputs.get("size", 0)) != int(new_inputs.get("size", 0))  # Compare as ints
        read_only_changed = old_inputs.get("read_only") != new_inputs.get("read_only")
        endpoint_changed = old_inputs.get("endpoint") != new_inputs.get("endpoint")

        return pulumi.dynamic.DiffResult(
            changes=name_changed or size_changed or read_only_changed or endpoint_changed,
            replaces=[],
            delete_before_replace=False
        )

