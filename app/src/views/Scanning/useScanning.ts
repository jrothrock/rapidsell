import axios from 'axios';
import { toastController } from '@ionic/vue';
import { Camera, CameraResultType, CameraSource } from '@capacitor/camera';
import { useAuthStore } from '@/stores';
import type { PresignResponse } from "@/api/scanning/Presign";
import type { Ref } from "vue";

const PRESIGN_URL = `${import.meta.env.VITE_BASE_URL}/scanning/presign`;

export type UserPhoto = {
  filepath?: string;
  dataUrl?: string;
}

async function dataURLtoBlob(dataURI: string) {
  // convert base64 to raw binary data held in a string
  // doesn't handle URLEncoded DataURIs - see SO answer #6850276 for code that does this
  var byteString = atob(dataURI.split(',')[1]);

  // separate out the mime component
  var mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0];

  // write the bytes of the string to an ArrayBuffer
  var ab = new ArrayBuffer(byteString.length);

  // create a view into the buffer
  var ia = new Uint8Array(ab);

  // set the bytes of the buffer to the correct values
  for (var i = 0; i < byteString.length; i++) {
      ia[i] = byteString.charCodeAt(i);
  }

  // write the ArrayBuffer to a blob, and you're done
  var blob = new Blob([ab], {type: mimeString});
  return blob;

}

async function presign(mimetype: string): Promise<string> {
  const store = useAuthStore();
  const config = {
    headers: {
      "X-ACCESS-TOKEN": store.getAccessToken,
      "Authorization": `Bearer ${store.getIdToken}`,
      "X-MIME-TYPE": mimetype
    }
  };
  const response = await axios.get(PRESIGN_URL, config);
  const data: PresignResponse = response.data;
  return data.url;
}

async function takePhoto(photo: Ref<UserPhoto | undefined>) {
  const capturedPhoto = await Camera.getPhoto({
    resultType: CameraResultType.DataUrl,
    source: CameraSource.Camera,
    quality: 100,
  });
  
  const fileName = Date.now() + '.jpeg';
  const savedFileImage: UserPhoto = {
    filepath: fileName,
    dataUrl: capturedPhoto.dataUrl,
  };

  photo.value = savedFileImage;
}

async function uploadPhoto(photo: Ref<UserPhoto | undefined>) {
  const dataUrl: string = (photo as Ref<UserPhoto>).value.dataUrl as string;
  const blobData = await dataURLtoBlob(dataUrl);

  try {
    const presignedUrl = await presign(blobData.type);
    
    await axios.put(presignedUrl, blobData, {
      headers: {
        'Content-Type': blobData.type
      }
    });

    const toast = await toastController.create({
      message: 'Upload Succeeded.',
      duration: 2500,
      position: 'top',
      color: 'success',
    });

    await toast.present();
  } catch {
    const toast = await toastController.create({
      message: 'Failed to upload photo.',
      duration: 2500,
      position: 'top',
      color: 'danger',
    });

    await toast.present();
  } 
}

export function useScanning(photo: Ref<UserPhoto | undefined>) {
  return {
    takePhoto: () => takePhoto(photo),
    uploadPhoto: () => uploadPhoto(photo),
  };
}
