class CarouselController {
    constructor(contenedorId, intervaloMs = 5000) {
        const contenedor = document.getElementById(contenedorId);
        if (!contenedor) return;
        this.slides = contenedor.querySelectorAll('.slide');
        this.indiceActual = 0;
        if (this.slides.length > 1) setInterval(() => this.siguienteSlide(), intervaloMs);
    }
    siguienteSlide() {
        this.slides[this.indiceActual].classList.remove('activo');
        this.indiceActual = (this.indiceActual + 1) % this.slides.length;
        this.slides[this.indiceActual].classList.add('activo');
    }
}

class UIController {
    constructor() {
        this.elementos = document.querySelectorAll('.fade-in');
        this.iniciarObservador();
    }
    iniciarObservador() {
        const observer = new IntersectionObserver((entradas) => {
            entradas.forEach(entrada => {
                if (entrada.isIntersecting) {
                    entrada.target.classList.add('visible');
                    observer.unobserve(entrada.target);
                }
            });
        }, { threshold: 0.1 });
        this.elementos.forEach(el => observer.observe(el));
    }
}

class FormController {
    constructor(formId, endpoint) {
        this.formulario = document.getElementById(formId);
        this.endpoint = endpoint;
        this.cajaRespuesta = document.getElementById('form-respuesta');
        if (this.formulario) this.formulario.addEventListener('submit', (e) => this.enviarDatos(e));
    }
    async enviarDatos(e) {
        e.preventDefault();
        const boton = this.formulario.querySelector('button');
        boton.innerText = 'Enviando...'; boton.disabled = true;
        try {
            const formData = new FormData(this.formulario);
            const respuesta = await fetch(this.endpoint, { method: 'POST', body: formData });
            const data = await respuesta.json();
            this.cajaRespuesta.style.color = respuesta.ok ? 'var(--acento-primario)' : '#ff6b6b';
            this.cajaRespuesta.innerText = data.mensaje;
            if (respuesta.ok) this.formulario.reset();
        } catch (error) {
            this.cajaRespuesta.style.color = '#ff6b6b';
            this.cajaRespuesta.innerText = "Error de red. Intenta nuevamente.";
        } finally {
            boton.innerText = 'Enviar Mensaje'; boton.disabled = false;
        }
    }
}

class Engine3D {
    constructor(containerId, objPath) {
        this.container = document.getElementById(containerId);
        this.objPath = objPath;
        if (this.container) this.init();
    }
    init() {
        this.scene = new THREE.Scene();
        this.camera = new THREE.PerspectiveCamera(45, this.container.clientWidth / this.container.clientHeight, 0.1, 1000);
        this.camera.position.set(0, 5, 15);

        this.renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
        this.renderer.setSize(this.container.clientWidth, this.container.clientHeight);
        this.renderer.setPixelRatio(window.devicePixelRatio);
        this.container.appendChild(this.renderer.domElement);

        this.controls = new THREE.OrbitControls(this.camera, this.renderer.domElement);
        this.controls.enableDamping = true;
        this.controls.autoRotate = true;
        this.controls.autoRotateSpeed = 1.5;

        const ambient = new THREE.AmbientLight(0xffffff, 0.6);
        const directional1 = new THREE.DirectionalLight(0x0984e3, 0.7);
        directional1.position.set(5, 10, 7);
        const directional2 = new THREE.DirectionalLight(0xffffff, 0.4);
        directional2.position.set(-5, -5, -5);
        this.scene.add(ambient, directional1, directional2);

        const loader = new THREE.OBJLoader();
        loader.load(this.objPath, (object) => {
            const material = new THREE.MeshStandardMaterial({ color: 0x555555, roughness: 0.3, metalness: 0.6 });
            object.traverse((child) => { if (child.isMesh) child.material = material; });
            const box = new THREE.Box3().setFromObject(object);
            const center = box.getCenter(new THREE.Vector3());
            object.position.sub(center);
            object.position.y -= 13;
            object.scale.set(0.1, 0.1, 0.1);
            this.scene.add(object);
        });

        // Este evento asegura que el 3D sea autoajustable al rotar la pantalla del móvil
        window.addEventListener('resize', () => this.onResize());
        this.animate();
    }
    animate() {
        requestAnimationFrame(() => this.animate());
        this.controls.update();
        this.renderer.render(this.scene, this.camera);
    }
    onResize() {
        this.camera.aspect = this.container.clientWidth / this.container.clientHeight;
        this.camera.updateProjectionMatrix();
        this.renderer.setSize(this.container.clientWidth, this.container.clientHeight);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new CarouselController('carrusel-fondo', 4000);
    new UIController();
    new FormController('form-contacto', '/api/contacto');
    new Engine3D('contenedor-3d', '/static/modelos_3d/Boquilla_NSF.obj');
});