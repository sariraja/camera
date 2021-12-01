var constraints ={video: {facingMode: "user"}, audio:false};
const cameraView = document.querySelector("#Camer--view"),
       cameraOutput =document.querySelector("camera--output"),
       CameraSensor= document.querySelector("#camera--sensor"),
       cameraTrigger=document.querySelector("#camera--trigger")


 function CameraStart() {
     navigator.mediaDevices
          .getUserMedia(constraints)
          .then(function(stream){
          track =stream.getTracks()[0];
          cameraView.srcObject = stream;
          })
     .catch(function(error){
         console.error("Oops.something is broken.",error);

     });
    }
cameraTrigger.onclick =function() {
         cameraSensor.width = cameraView.videoWidth;
         cameraSensor.height =cameraView.videoHeight;
         cameraSensor.getContext("2d").drawimage(cameraView,0,0);
         cameraOutput .scr = cameraSensor.to DataURL("image/webp");
         cameraOUtput.classList.add("taken");
     };

   window.addEventListener("load", cameraStart,false);